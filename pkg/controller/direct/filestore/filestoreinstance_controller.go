// Copyright 2026 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package filestore

import (
	"context"
	"fmt"

	gcp "cloud.google.com/go/filestore/apiv1"
	pb "cloud.google.com/go/filestore/apiv1/filestorepb"
	"google.golang.org/api/option"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/types/known/fieldmaskpb"
	"k8s.io/apimachinery/pkg/apis/meta/v1/unstructured"
	"k8s.io/apimachinery/pkg/runtime"
	"k8s.io/klog/v2"

	krm "github.com/GoogleCloudPlatform/k8s-config-connector/apis/filestore/v1beta1"
	"github.com/GoogleCloudPlatform/k8s-config-connector/pkg/config"
	"github.com/GoogleCloudPlatform/k8s-config-connector/pkg/controller/direct"
	"github.com/GoogleCloudPlatform/k8s-config-connector/pkg/controller/direct/common"
	"github.com/GoogleCloudPlatform/k8s-config-connector/pkg/controller/direct/directbase"
	"github.com/GoogleCloudPlatform/k8s-config-connector/pkg/controller/direct/registry"
	"github.com/GoogleCloudPlatform/k8s-config-connector/pkg/controller/direct/tags"
	"github.com/GoogleCloudPlatform/k8s-config-connector/pkg/structuredreporting"
)

func init() {
	registry.RegisterModel(krm.FilestoreInstanceGVK, newFilestoreInstanceModel)
}

func newFilestoreInstanceModel(ctx context.Context, config *config.ControllerConfig) (directbase.Model, error) {
	return &filestoreInstanceModel{config: config}, nil
}

type filestoreInstanceModel struct {
	config *config.ControllerConfig
}

// model implements the Model interface.
var _ directbase.Model = &filestoreInstanceModel{}

type filestoreInstanceAdapter struct {
	id *krm.FilestoreInstanceIdentity

	desired *pb.Instance
	actual  *pb.Instance

	client *gcp.CloudFilestoreManagerClient
}

// adapter implements the Adapter interface.
var _ directbase.Adapter = &filestoreInstanceAdapter{}

func (m *filestoreInstanceModel) client(ctx context.Context) (*gcp.CloudFilestoreManagerClient, error) {
	var opts []option.ClientOption
	opts, err := m.config.RESTClientOptions()
	if err != nil {
		return nil, err
	}
	gcpClient, err := gcp.NewCloudFilestoreManagerRESTClient(ctx, opts...)
	if err != nil {
		return nil, fmt.Errorf("building FilestoreInstance client: %w", err)
	}
	return gcpClient, err
}

// AdapterForObject implements the Model interface.
func (m *filestoreInstanceModel) AdapterForObject(ctx context.Context, op *directbase.AdapterForObjectOperation) (directbase.Adapter, error) {
	u := op.GetUnstructured()
	kube := op.Reader

	gcpClient, err := m.client(ctx)
	if err != nil {
		return nil, err
	}

	obj := &krm.FilestoreInstance{}
	if err := runtime.DefaultUnstructuredConverter.FromUnstructured(u.Object, &obj); err != nil {
		return nil, fmt.Errorf("error converting to %T: %w", obj, err)
	}

	id, err := obj.GetIdentity(ctx, kube)
	if err != nil {
		return nil, err
	}

	if err := common.NormalizeReferences(ctx, kube, obj, nil); err != nil {
		return nil, fmt.Errorf("normalizing references: %w", err)
	}

	mapCtx := &direct.MapContext{}
	desired := FilestoreInstanceSpec_ToProto(mapCtx, &obj.Spec)
	if mapCtx.Err() != nil {
		return nil, mapCtx.Err()
	}

	return &filestoreInstanceAdapter{
		id:      id.(*krm.FilestoreInstanceIdentity),
		desired: desired,
		client:  gcpClient,
	}, nil
}

func (m *filestoreInstanceModel) AdapterForURL(ctx context.Context, url string) (directbase.Adapter, error) {
	return nil, nil
}

// Find implements the Adapter interface.
func (a *filestoreInstanceAdapter) Find(ctx context.Context) (bool, error) {
	if a.id.Instance == "" {
		return false, nil
	}

	req := &pb.GetInstanceRequest{
		Name: a.id.String(),
	}
	instance, err := a.client.GetInstance(ctx, req)
	if err != nil {
		if direct.IsNotFound(err) {
			return false, nil
		}
		return false, err
	}

	a.actual = instance

	return true, nil
}

// Delete implements the Adapter interface.
func (a *filestoreInstanceAdapter) Delete(ctx context.Context, deleteOp *directbase.DeleteOperation) (bool, error) {
	if a.id.Instance == "" {
		return false, nil
	}

	req := &pb.DeleteInstanceRequest{
		Name: a.id.String(),
	}

	op, err := a.client.DeleteInstance(ctx, req)
	if err != nil {
		if direct.IsNotFound(err) {
			return false, nil
		}
		return false, fmt.Errorf("deleting filestoreInstance %s: %w", a.id.String(), err)
	}

	if err := op.Wait(ctx); err != nil {
		return false, fmt.Errorf("waiting for filestoreInstance delete %s: %w", a.id.String(), err)
	}

	return true, nil
}

func (a *filestoreInstanceAdapter) Export(ctx context.Context) (*unstructured.Unstructured, error) {
	return nil, nil
}

// Create implements the Adapter interface.
func (a *filestoreInstanceAdapter) Create(ctx context.Context, createOp *directbase.CreateOperation) error {
	u := createOp.GetUnstructured()

	log := klog.FromContext(ctx)
	log.V(0).Info("creating object", "u", u)

	parent := a.id.ParentString()

	req := &pb.CreateInstanceRequest{
		Parent:     parent,
		InstanceId: a.id.Instance,
		Instance:   a.desired,
	}

	log.V(0).Info("making filestore CreateInstance call", "request", req)

	op, err := a.client.CreateInstance(ctx, req)
	if err != nil {
		return fmt.Errorf("creating instance: %w", err)
	}

	created, err := op.Wait(ctx)
	if err != nil {
		return fmt.Errorf("waiting for filestoreInstance create %s: %w", a.id.String(), err)
	}

	log.V(0).Info("created filestoreInstance", "instance", created)

	status := &krm.FilestoreInstanceStatus{}

	mapCtx := &direct.MapContext{}
	if err := a.populateStatus(ctx, status, created, mapCtx); err != nil {
		return err
	}
	if mapCtx.Err() != nil {
		return mapCtx.Err()
	}

	status.ExternalRef = direct.LazyPtr(a.id.String())

	return createOp.UpdateStatus(ctx, status, nil)
}

// Update implements the Adapter interface.
func (a *filestoreInstanceAdapter) Update(ctx context.Context, updateOp *directbase.UpdateOperation) error {
	u := updateOp.GetUnstructured()

	log := klog.FromContext(ctx)
	log.V(0).Info("updating object", "u", u)

	diffs, err := compareFilestoreInstance(ctx, a.actual, a.desired)
	if err != nil {
		return fmt.Errorf("comparing actual and desired FilestoreInstance: %w", err)
	}

	var latest *pb.Instance
	if diffs.HasDiff() {
		diffs.Object = u
		structuredreporting.ReportDiff(ctx, diffs)

		var paths []string
		for _, field := range diffs.Fields {
			if field.ProtoFieldDescriptor == nil {
				return fmt.Errorf("unexpected diff field without proto descriptor: %s", field.ID)
			}
			paths = append(paths, string(field.ProtoFieldDescriptor.Name()))
		}

		req := &pb.UpdateInstanceRequest{
			Instance: a.desired,
			UpdateMask: &fieldmaskpb.FieldMask{
				Paths: paths,
			},
		}

		req.Instance.Name = a.id.String()

		log.V(0).Info("making filestore UpdateInstance call", "request", req)

		op, err := a.client.UpdateInstance(ctx, req)
		if err != nil {
			return err
		}

		updated, err := op.Wait(ctx)
		if err != nil {
			return fmt.Errorf("waiting for filestoreInstance update %s: %w", a.id.String(), err)
		}
		log.V(0).Info("updated filestoreInstance", "instance", updated)

		latest = updated
	} else {
		latest = a.actual
	}

	status := &krm.FilestoreInstanceStatus{}
	mapCtx := &direct.MapContext{}
	if err := a.populateStatus(ctx, status, latest, mapCtx); err != nil {
		return err
	}
	if mapCtx.Err() != nil {
		return mapCtx.Err()
	}

	status.ExternalRef = direct.LazyPtr(a.id.String())

	return updateOp.UpdateStatus(ctx, status, nil)
}

func (a *filestoreInstanceAdapter) populateStatus(ctx context.Context, status *krm.FilestoreInstanceStatus, actual *pb.Instance, mapCtx *direct.MapContext) error {
	status.CreateTime = direct.StringTimestamp_FromProto(mapCtx, actual.GetCreateTime())
	if actual.GetEtag() != "" {
		status.Etag = direct.LazyPtr(actual.GetEtag())
	}
	status.State = direct.Enum_FromProto(mapCtx, actual.GetState())
	if actual.GetStatusMessage() != "" {
		status.StatusMessage = direct.LazyPtr(actual.GetStatusMessage())
	}
	return nil
}

func compareFilestoreInstance(ctx context.Context, actual, desired *pb.Instance) (*structuredreporting.Diff, error) {
	var maskedActual *pb.Instance
	{
		// A "trick" to only compare spec fields - round trip via the spec
		mapCtx := &direct.MapContext{}
		spec := FilestoreInstanceSpec_FromProto(mapCtx, actual)
		if mapCtx.Err() != nil {
			return nil, mapCtx.Err()
		}
		maskedActual = FilestoreInstanceSpec_ToProto(mapCtx, spec)
		if mapCtx.Err() != nil {
			return nil, mapCtx.Err()
		}
	}

	desired = proto.Clone(desired).(*pb.Instance)

	diffs, _, err := tags.DiffForTopLevelFields(ctx, desired.ProtoReflect(), maskedActual.ProtoReflect())
	if err != nil {
		return nil, err
	}
	return diffs, nil
}
