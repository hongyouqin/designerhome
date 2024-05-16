package midjourney

import (
	"context"

	"github.com/gogf/gf/v2/errors/gcode"
	"github.com/gogf/gf/v2/errors/gerror"

	"designer-service/api/midjourney/v1"
)

func (c *ControllerV1) ImagineCmd(ctx context.Context, req *v1.ImagineCmdReq) (res *v1.ImagineCmdRes, err error) {
	return nil, gerror.NewCode(gcode.CodeNotImplemented)
}
