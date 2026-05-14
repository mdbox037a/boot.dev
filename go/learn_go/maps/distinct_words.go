package main

import "strings"

func countDistinctWords(messages []string) int {
	distinctWords := make(map[string]struct{})
	for _, msg := range messages {
		for _, word := range strings.Fields(msg) {
			lower_word := strings.ToLower(word)
			if _, ok := distinctWords[lower_word]; !ok {
				distinctWords[lower_word] = struct{}{}
			}
		}
	}
	return len(distinctWords)
}
