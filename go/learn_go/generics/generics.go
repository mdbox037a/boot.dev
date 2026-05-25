package main

func getLast[T any](s []T) T {
	var last T
	if len(s) > 0 {
		last = s[len(s)-1]
	}
	return last
}
