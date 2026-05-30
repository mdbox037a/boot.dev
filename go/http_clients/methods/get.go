package main

import (
	"encoding/json"
	"net/http"
)

func getUsers(url string) ([]User, error) {
	res, err := http.Get(url)
	if err != nil {
		return nil, err
	}

	defer res.Body.Close()

	users := []User{}
	decoder := json.NewDecoder(res.Body)
	if err := decoder.Decode(&users); err != nil {
		return nil, err
	}

	return users, nil
}
