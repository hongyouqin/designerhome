package cmd

import (
	"context"
	"net/url"
	"strings"

	"github.com/gogf/gf/os/glog"
	"github.com/gogf/gf/v2/frame/g"
	"github.com/gogf/gf/v2/net/ghttp"
	"github.com/gogf/gf/v2/os/gcmd"

	"designer-service/internal/controller/hello"
	cmj "designer-service/internal/controller/midjourney"
)

var (
	Main = gcmd.Command{
		Name:  "main",
		Usage: "main",
		Brief: "start http server",
		Func: func(ctx context.Context, parser *gcmd.Parser) (err error) {
			//日志初始化
			g.Log().SetFlags(glog.F_ASYNC | glog.F_TIME_DATE | glog.F_TIME_TIME | glog.F_FILE_LONG)
			// 初始化代理

			proxy := NewProxyServer()

			s := g.Server()
			s.Group("/proxy", func(group *ghttp.RouterGroup) {
				group.ALL("/*", func(r *ghttp.Request) {
					proxyUrl, _ := g.Cfg().Get(ctx, "proxy.url")
					origPath := strings.TrimPrefix(r.URL.Path, "/proxy")
					target := proxyUrl.String() + origPath + "?" + r.URL.RawQuery
					parseURL, err := url.Parse(target)
					if err != nil {
						r.Response.WriteStatusExit(500, "Failed to parse target URL")
						g.Log().Error(ctx, target, " Failed to parse target URL")
						return
					}
					r.Request.URL = parseURL
					g.Log().Info(ctx, "go proxy： ", target)
					proxy.ServeHTTP(r.Response.Writer, r.Request)
				})
			})
			s.Group("/", func(group *ghttp.RouterGroup) {
				group.Group("/mj", func(group *ghttp.RouterGroup) {
					//mj模型
					group.Middleware(ghttp.MiddlewareHandlerResponse)
					group.Bind(cmj.NewV1())
				})
				group.Middleware(ghttp.MiddlewareHandlerResponse)
				group.Bind(
					hello.NewV1(),
				)
			})
			s.Run()
			return nil
		},
	}
)
