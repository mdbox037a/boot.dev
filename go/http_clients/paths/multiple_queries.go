package main

func fetchTasks(baseURL, availability string) []Issue {
	sort := "estimate"
	var limit string
	switch availability {
	case "Low":
		limit = "1"
	case "Medium":
		limit = "3"
	case "High":
		limit = "5"
	default:
		limit = "0"
	}

	fullURL := baseURL + "?sort=" + sort + "&limit=" + limit
	return getIssues(fullURL)
}
