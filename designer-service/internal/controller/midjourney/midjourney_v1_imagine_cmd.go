package midjourney

import (
	"context"

	"github.com/gogf/gf/v2/errors/gcode"
	"github.com/gogf/gf/v2/errors/gerror"
	"github.com/gogf/gf/v2/frame/g"

	v1 "designer-service/api/midjourney/v1"
	"designer-service/internal/model"
	"designer-service/internal/service"
)

func (c *ControllerV1) ImagineCmd(ctx context.Context, req *v1.ImagineCmdReq) (res *v1.ImagineCmdRes, err error) {
	input := model.TriggerImageInput{
		Prompt:   req.Prompt,
		ImageUrl: req.ImageUrl,
	}
	out, err := service.MjCmd().GenImage(ctx, input)
	if err != nil {
		g.Log().Error(ctx, err)
		return nil, gerror.NewCode(gcode.CodeInternalError, err.Error())
	}
	if out != nil {
		return nil, gerror.NewCode(gcode.New(out.Code, out.Message, ""))
	}
	return res, nil
}
