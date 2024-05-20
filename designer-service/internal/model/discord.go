package model

import (
	"github.com/gogf/gf/v2/frame/g"
)

// discord 操作
func TriggerPayloadWrap(t int, data g.Map) *g.Map {
	payload := g.Map{
		"type":           t,
		"application_id": "936929561302675456",
		"guild_id":       "",
		"channel_id":     "",
		"data":           data,
	}
	return &payload
}
