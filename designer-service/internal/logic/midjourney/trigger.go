package midjourney

import (
	"context"
	"designer-service/internal/model"
	"designer-service/internal/service"

	"github.com/gogf/gf/v2/frame/g"
)

// mj服务
type sMjCmd struct {
}

func New() service.IMjCmd {
	return &sMjCmd{}
}

func init() {
	service.RegisterMjCmd(New())
}

func (s *sMjCmd) GenImage(ctx context.Context, input model.TriggerImageInput) (out *model.TriggerImageOutput, err error) {
	trigger_url, _ := g.Cfg().Get(ctx, "discord.trigger_url")
	user_token, _ := g.Cfg().Get(ctx, "discord.user_token")
	g.Log().Debug(ctx, "trigger_url: ", trigger_url, "user_token:", user_token)
	client := g.Client()
	client.SetHeader("Content-Type", "application/json")
	client.SetHeader("Authorization", user_token.String())
	payload := model.TriggerPayloadWrap(2, g.Map{
		"version": "1",
		"id":      "123",
		"name":    "imagine",
		"options": []map[string]interface{}{
			{
				"name":  "prompt",
				"type":  3,
				"value": input.Prompt,
			},
		},
	})
	g.Log().Debug(ctx, "payload: ", payload)
	r, err := client.Post(ctx, trigger_url.String(), payload)
	if err != nil {
		return nil, err
	}
	defer r.Close()
	resultByte := r.ReadAll()
	result := string(resultByte)
	g.Log().Info(ctx, "result: ", result)
	return nil, nil
}
