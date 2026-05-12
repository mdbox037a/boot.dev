package main

import "errors"

func deleteIfNecessary(users map[string]user, name string) (deleted bool, err error) {
	temp, ok := users[name]
	if !ok {
		return false, errors.New("not found")
	} else if !temp.scheduledForDeletion {
		return false, nil
	} else {
		delete(users, name)
		return true, nil
	}
}

type user struct {
	name                 string
	number               int
	scheduledForDeletion bool
}
