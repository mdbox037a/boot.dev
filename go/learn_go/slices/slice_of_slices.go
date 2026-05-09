package main

func createMatrix(rows, cols int) [][]int {
	chart := [][]int{}
	for i := range rows {
		holderRow := []int{}
		for j := range cols {
			holderRow = append(holderRow, i*j)
		}
		chart = append(chart, holderRow)
	}
	return chart
}
