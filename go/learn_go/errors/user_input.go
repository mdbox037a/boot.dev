package main

import (
	"errors"
)

func validateStatus(status string) error {
	var err error = nil
	if status == "" {
		err = errors.New("status cannot be empty")
		return err
	}
	if len(status) > 140 {
		err = errors.New("status exceeds 140 characters")
		return err
	}
	return err
}
