void swap_strings(char **a, char **b) {
  char *temp;
  temp = *a;
  *a = *b;
  *b = temp;
}
