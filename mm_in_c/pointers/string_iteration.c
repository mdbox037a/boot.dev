#include <stdio.h>

int main(void) {
	char *my_string = "hello";
	int i;

	for (i = 0; *(my_string + i); i++) {
		printf("%c\n", *(my_string + i));
	}
	return 0;
}
