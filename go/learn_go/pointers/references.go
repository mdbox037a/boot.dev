package main

import (
	"strings"
)

func removeProfanity(message *string) {
	messageCopy := *message
	badWords := []string{"fubb", "shiz", "witch"}
	for _, bw := range badWords {
		stars := strings.Repeat("*", len(bw))
		messageCopy = strings.ReplaceAll(messageCopy, bw, stars)
	}
	*message = messageCopy
}
