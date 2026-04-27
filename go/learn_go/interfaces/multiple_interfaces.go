package main

import "fmt"

func (e email) cost() int {
	cost := 0
	if e.isSubscribed == false {
		cost = 5
	} else {
		cost = 2
	}
	return len(e.body) * cost
}

func (e email) format() string {
	status := ""
	if e.isSubscribed == true {
		status = "Subscribed"
	} else {
		status = "Not Subscribed"
	}
	return fmt.Sprintf("'%s' | %s", e.body, status)
}

type expense interface {
	cost() int
}

type formatter interface {
	format() string
}

type email struct {
	isSubscribed bool
	body         string
}
