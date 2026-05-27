package main

import (
	"encoding/json"
)

func marshalAll[T any](items []T) ([][]byte, error) {
	data := make([][]byte, len(items))
	for i, item := range items {
		temp, err := json.Marshal(item)
		if err != nil {
			return nil, err
		}
		data[i] = temp
	}
	return data, nil
}
