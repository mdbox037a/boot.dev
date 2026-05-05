package main

func bulkSend(numMessages int) float64 {
	cost := 0.0
	for i, fee := 0, 0.0; i < numMessages; i, fee = i+1, fee+0.01 {
		cost += 1.0 + fee
	}
	return cost
}
