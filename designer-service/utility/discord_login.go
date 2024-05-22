package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
)

type LoginResponse struct {
	Token string `json:"token"`
}

func main() {
	email := "yang.qq123@163.com"
	password := "qinhy0904"

	loginURL := "https://discord.com/api/v9/auth/login"
	loginData := map[string]string{
		"login":    email,
		"password": password,
	}

	jsonData, err := json.Marshal(loginData)
	if err != nil {
		fmt.Println("Error encoding login data:", err)
		return
	}

	resp, err := http.Post(loginURL, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error logging in to Discord:", err)
		return
	}
	defer resp.Body.Close()

	var loginResp LoginResponse
	err = json.NewDecoder(resp.Body).Decode(&loginResp)
	if err != nil {
		fmt.Println("Error decoding login response:", err)
		return
	}

	fmt.Println("Token:", loginResp.Token)
}
