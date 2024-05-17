package midjourney

import "context"

// mj服务
type sMjCmd struct {
}

func New() *sMjCmd {
	return &sMjCmd{}
}

func (s *sMjCmd) GenImage(ctx context.Context, input model.TriggerImageInput) (out *model.TriggerImageOutput, err error) {
	
	reutrn nil , nil
}
