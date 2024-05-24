package model

import (
	"context"

	"github.com/gogf/gf/v2/frame/g"
)

// discord 操作
func TriggerPayloadWrap(typ int, data g.Map) *g.Map {
	gid, _ := g.Cfg().Get(context.TODO(), "discord.guild_id")
	cid, _ := g.Cfg().Get(context.TODO(), "discord.channel_id")
	aid, _ := g.Cfg().Get(context.TODO(), "discord.application_id")
	sid, _ := g.Cfg().Get(context.TODO(), "discord.session_id")

	payload := g.Map{
		"type":           typ,
		"application_id": aid.String(),
		"session_id":     sid.String(),
		"guild_id":       gid.String(),
		"channel_id":     cid.String(),
		"data":           data,
	}
	return &payload
}
