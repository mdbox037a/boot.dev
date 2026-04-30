package main

func sendMessage(format formatter) string {
	return format.format() // Adjusted to call Format without an argument
}
