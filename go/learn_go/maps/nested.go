package main

func getNameCounts(names []string) map[rune]map[string]int {
	nestedMap := map[rune]map[string]int{}
	for _, name := range names {
		runes := []rune(name)
		letter := runes[0]
		if section, ok := nestedMap[letter]; ok {
			section[name]++
		} else {
			section = map[string]int{}
			nestedMap[letter] = section
			section[name]++
		}
	}
	return nestedMap
}
