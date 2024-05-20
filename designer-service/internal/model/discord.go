package model

import (
	"context"

	"github.com/gogf/gf/v2/frame/g"
)

// discord 操作
func TriggerPayloadWrap(typ int, data g.Map) *g.Map {
	gid, _ := g.Cfg().Get(context.TODO(), "discord.guild_id")
	cid, _ := g.Cfg().Get(context.TODO(), "discord.channel_id")

	payload := g.Map{
		"type":           typ,
		"application_id": "936929561302675456",
		"guild_id":       gid,
		"channel_id":     cid,
		"data":           data,
	}
	return &payload
}
