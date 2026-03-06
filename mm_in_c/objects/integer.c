#include "snekobject.h"
#include <stdlib.h>

snek_object_t *new_snek_integer(int value) {
        snek_object_t *new_int = malloc(sizeof(snek_object_t));
        if (new_int == NULL) {
                return NULL;
        }
        new_int->kind = INTEGER;
        new_int->data = (snek_object_data_t)value;
        return new_int;
}
