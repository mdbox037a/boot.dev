package main

func isValidPassword(password string) bool {
	if len(password) < 5 || len(password) > 12 {
		return false
	}
	hasUpperCase := false
	hasDigit := false
	for _, char := range password {
		if char >= 'A' && char <= 'Z' {
			hasUpperCase = true
		}
		if char >= '0' && char <= '9' {
			hasDigit = true
		}
		if hasUpperCase && hasDigit {
			return true
		}
	}
	return false
}
