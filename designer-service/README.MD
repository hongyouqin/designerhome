# GoFrame Template For SingleRepo

Quick Start:

- https://goframe.org/pages/viewpage.action?pageId=1114399

# 交叉编译(用于在 liunx 上部署)

GOOS=linux GOARCH=amd64 go build -o mj_server main.go
## 在windows上交叉编译
$env:CGO_ENABLED="0"
$env:GOOS="linux"
$env:GOARCH="amd64"
go build -o mj_server main.go
