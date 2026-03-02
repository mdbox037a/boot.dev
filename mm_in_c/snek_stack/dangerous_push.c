#include "snekstack.h"
#include "stdlib.h"

void scary_double_push(stack_t *s) {
  int i = 1337;
  stack_push(s, (void *)i);
  int *j = malloc(sizeof(int));
  *j = 1024;
  stack_push(s, j);
}
