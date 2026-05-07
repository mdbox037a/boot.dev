package main

type cost struct {
	day   int
	value float64
}

func getDayCosts(costs []cost, day int) []float64 {
	totals := make([]float64, 0, len(costs))
	for i := 0; i < len(costs); i++ {
		if costs[i].day == day {
			totals = append(totals, costs[i].value)
		}
	}
	return totals
}
