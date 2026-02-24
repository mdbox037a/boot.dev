#include "exercise.h"
#include <stdio.h>
#include <stdlib.h>

int *allocate_scalar_array(int size, int multiplier) {
    int i;
    
    int *ptr = malloc(size * sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    for (i = 0; i < size; i++) {
        *(ptr + i) = i * multiplier;
    }
    return ptr;
}