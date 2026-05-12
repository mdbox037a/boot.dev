package main

import (
	"errors"
)

func getUserMap(names []string, phoneNumbers []int) (map[string]user, error) {
	if len(names) != len(phoneNumbers) {
		return nil, errors.New("invalid sizes")
	}
	users := make(map[string]user)
	for i, key := range names {
		users[key] = user{name: key, phoneNumber: phoneNumbers[i]}
	}
	return users, nil
}

type user struct {
	name        string
	phoneNumber int
}
