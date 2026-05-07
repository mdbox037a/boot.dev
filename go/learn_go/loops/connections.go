package main

func countConnections(groupSize int) int {
	numConnections := 0
	for n := 0; n < groupSize; n++ {
		numConnections += n
	}
	return numConnections
}
