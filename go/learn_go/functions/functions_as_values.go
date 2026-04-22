package main

import "fmt"

func reformat(message string, formatter func(string) string) string {
	formatted := formatter(formatter(formatter(message)))
	return fmt.Sprintf("TEXTIO: %s", formatted)
}
