#include "exercise.h"
#include <stdio.h>
#include <string.h>

#define MAX_BUFFER_SIZE 64

int smart_append(TextBuffer *dest, const char *src) {
	if ((dest == NULL) || (src == NULL))
		return 1;

	int src_len = strlen(src);
	int dest_buff_remain = MAX_BUFFER_SIZE - (int)strlen(dest->buffer);

	printf("\nDEBUG: src_len: %d\n", src_len);
	printf("DEBUG: dest.length: %zu\n", dest->length);
	printf("DEBUG: dest_buff_remain: %d\n", dest_buff_remain);

	if ((int)strlen(src) > dest_buff_remain) {
		strncat(dest->buffer, src, dest_buff_remain - 1);
		dest->length = MAX_BUFFER_SIZE - 1;
		return 1;
	}

	else {
		strcat(dest->buffer, src);
		dest->length += src_len;
		return 0;
	}

	return 0;
}
