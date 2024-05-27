package model

// 用于文生图、图生图
type TriggerImageInput struct {
	Prompt   string `json:"prompt" dc:"文本关键词"`
	ImageUrl string `json:"image_url" dc:"图片地址，用于图生图"`
}

type TriggerImageOutput struct {
	Message string `json:"message" dc:"信息"`
	Code    int    `json:"code" dc:"返回码"`
}
