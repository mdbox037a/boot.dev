package main

func countReports(numSentCh chan int) int {
	numSent := 0
	for {
		v, ok := <-numSentCh
		if !ok {
			break
		}
		numSent += v
	}
	return numSent
}

func sendReports(numBatches int, ch chan int) {
	for i := 0; i < numBatches; i++ {
		numReports := i*23 + 32%17
		ch <- numReports
	}
	close(ch)
}
