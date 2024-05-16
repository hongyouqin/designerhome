// =================================================================================
// Code generated and maintained by GoFrame CLI tool. DO NOT EDIT.
// =================================================================================

package midjourney

import (
	"context"

	"designer-service/api/midjourney/v1"
)

type IMidjourneyV1 interface {
	ImagineCmd(ctx context.Context, req *v1.ImagineCmdReq) (res *v1.ImagineCmdRes, err error)
}
