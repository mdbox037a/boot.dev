#include <stdio.h>

void print_numbers(int start, int end) {
	int i;

	for (i = start; i <= end; i++)
		printf("%d\n", i);
}

void print_evens(int start, int end) {
    int i;
    
    for (i = start; i <= end; i++)
        printf("%d\n", 2 * i);
}