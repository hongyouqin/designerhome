package cmd

import (
	"github.com/elazarl/goproxy"
)

func NewProxyServer() *goproxy.ProxyHttpServer {
	proxy := goproxy.NewProxyHttpServer()
	proxy.Verbose = true
	return proxy
}
