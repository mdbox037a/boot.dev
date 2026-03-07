#include "snekobject.h"
#include <stdlib.h>

snek_object_t *new_snek_float(float value) {
        // ?
}

// don't touch below this line

snek_object_t *new_snek_integer(int value) {
        snek_object_t *obj = malloc(sizeof(snek_object_t));
        if (obj == NULL) {
                return NULL;
        }

        obj->kind = INTEGER;
        obj->data.v_int = value;
        return obj;
}
