package main

func updateCounts(messagedUsers []string, validUsers map[string]int) {
	for _, user := range messagedUsers {
		_, ok := validUsers[user]
		if ok {
			validUsers[user] += 1
		}
	}
}
