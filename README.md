# UI 设计师平台相关服务

# ui 设计

https://lanhuapp.com/link/#/invite?sid=lxwBWfXa
https://lanhuapp.com/web/#/item/project/stage?tid=50e351db-3638-40e1-8fd2-d84bd780b0b8&pid=7b2c3097-32ea-44df-82c3-20e4eee1046f
分享人: UI 设计
团队名称: 1 的团队
相关项目: AI

# 技术文档

## pip 清华镜像源

-i https://pypi.tuna.tsinghua.edu.cn/simple some-package

## discord.py 文档

https://discordpy.readthedocs.io/en/stable/api.html?highlight=on_message#discord.on_message

## 交互命令

https://github.com/discord/discord-api-docs/blob/main/docs/interactions/Application_Commands.md

## 导出环境包
pip freeze > requirements.txt

## nsq 教程

https://www.cnblogs.com/yezigege/p/13791476.html

## 远程端口映射
ssh -R 9914:47.101.161.124:9914 root@47.101.161.124

## ChatGPT&Midjounery 第三方技术文章

https://zhuanlan.zhihu.com/p/643189533

## git 操作

### 取消代理

git config --global --unset http.proxy
git config --global --unset https.proxy

## docker安装（centor）
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker

## 安装制定的docker-compose版本
sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose



