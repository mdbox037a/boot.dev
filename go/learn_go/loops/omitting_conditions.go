package main

func maxMessages(thresh int) int {
	available := thresh
	count := 0
	for cost := 100; available >= cost; cost++ {
		available -= cost
		count++
	}
	return count
}
