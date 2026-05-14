package main

import "strings"

func countDistinctWords(messages []string) int {
	distinctWords := make(map[string]struct{})
	for _, msg := range messages {
		for _, word := range strings.Fields(strings.ToLower(msg)) {
			distinctWords[word] = struct{}{}
		}
	}
	return len(distinctWords)
}
