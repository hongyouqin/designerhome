package model

// 用于文生图、图生图
type TriggerImageInput {
	Prompt string `json:"prompt" dc:"文本关键词"`
	ImageUrl string `json:"image_url" dc:"图片地址，用于图生图"`
}

type TriggerImageOutput {

}