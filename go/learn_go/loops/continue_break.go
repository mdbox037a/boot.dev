package main

import (
	"fmt"
	"math"
)

func printPrimes(max int) {
	if max >= 2 {
		isPrime := true
		fmt.Println(2)
		for n := 3; n <= max; n += 2 {
			isPrime = true
			for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
				if n%i == 0 {
					isPrime = false
					break
				}
			}
			if isPrime {
				fmt.Println(n)
			}
		}
	}
}

func test(max int) {
	fmt.Printf("Primes up to %v:\n", max)
	printPrimes(max)
	fmt.Println("===============================================================")
}

func main() {
	test(10)
	test(20)
	test(30)
}
