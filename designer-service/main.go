package main

import (
	_ "designer-service/internal/packed"

	_ "designer-service/internal/logic"

	"github.com/gogf/gf/v2/os/gctx"

	"designer-service/internal/cmd"
)

func main() {
	cmd.Main.Run(gctx.GetInitCtx())
}
