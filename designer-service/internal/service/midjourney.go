// ================================================================================
// Code generated and maintained by GoFrame CLI tool. DO NOT EDIT.
// You can delete these comments if you wish manually maintain this interface file.
// ================================================================================

package service

import (
	"context"
)

type (
	IMjCmd interface {
		GenImage(ctx context.Context, input model.TriggerImageInput) (out *model.TriggerImageOutput, err error)
	}
)

var (
	localMjCmd IMjCmd
)

func MjCmd() IMjCmd {
	if localMjCmd == nil {
		panic("implement not found for interface IMjCmd, forgot register?")
	}
	return localMjCmd
}

func RegisterMjCmd(i IMjCmd) {
	localMjCmd = i
}
