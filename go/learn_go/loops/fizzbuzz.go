package main

import "fmt"

func fizzbuzz() {
	threer := 0
	fiver := 0
	for n := 1; n < 101; n++ {
		threer = n % 3
		fiver = n % 5

		if threer == 0 && fiver == 0 {
			fmt.Println("fizzbuzz")
		} else if threer == 0 {
			fmt.Println("fizz")
		} else if fiver == 0 {
			fmt.Println("buzz")
		} else {
			fmt.Println(n)
		}
	}
}

func main() {
	fizzbuzz()
}
