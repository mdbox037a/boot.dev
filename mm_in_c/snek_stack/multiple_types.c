#include "snekstack.h"
#include "stdlib.h"
#include <string.h>

void stack_push_multiple_types(stack_t *s) {
        float *i = malloc(sizeof(float));
        *i = 3.14;
        stack_push(s, i);
        char *message = "Sneklang is blazingly slow!";
        int message_len = strlen(message);
        char *j = malloc((message_len + 1) * sizeof(char));
        strcpy(j, message);
        stack_push(s, j);
}
