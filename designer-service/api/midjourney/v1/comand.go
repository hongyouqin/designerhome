package v1

// 文生图、图生图指令
type ImagineCmdReq struct {
	g.Meta `path:"/image" tags:"mj" method:"post" summary:"文生图、图生图midjourney"`
	Prompt string `json:"prompt" dc:"文本关键词"
	ImageUrl string `json:"image_url" dc:"图片地址，用于图生图"`
} 

type ImagineCmdRes struct {
	
}

