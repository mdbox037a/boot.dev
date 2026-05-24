package main

func concurrentFib(n int) []int {
	numCh := make(chan int)
	go fibonacci(n, numCh)

	var sequence []int
	for fibNum := range numCh {
		sequence = append(sequence, fibNum)
	}
	return sequence
}

func fibonacci(n int, ch chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		ch <- x
		x, y = y, x+y
	}
	close(ch)
}
