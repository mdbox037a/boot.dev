package main

func getNameCounts(names []string) map[rune]map[string]int {
	nameCounts := make(map[rune]map[string]int)
	for _, name := range names {
		firstLetter := []rune(name)[0]
		if _, ok := nameCounts[firstLetter]; !ok {
			nameCounts[firstLetter] = make(map[string]int)
		}
		nameCounts[firstLetter][name]++
	}
	return nameCounts
}
