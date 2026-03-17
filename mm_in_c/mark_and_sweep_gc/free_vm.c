#include "stack.h"
#include "vm.h"

void vm_free(vm_t *vm) {
        void *tmp;
        while ((tmp = stack_pop(vm->frames)) != NULL) {
                frame_free(tmp);
        }
        stack_free(vm->frames);
        while ((tmp = stack_pop(vm->objects)) != NULL) {
                snek_object_free(tmp);
        }
        stack_free(vm->objects);
        free(vm);
}

vm_t *vm_new() {
        vm_t *vm = malloc(sizeof(vm_t));
        if (vm == NULL) {
                return NULL;
        }

        vm->frames = stack_new(8);
        vm->objects = stack_new(8);
        return vm;
}

void vm_track_object(vm_t *vm, snek_object_t *obj) {
        stack_push(vm->objects, obj);
}

void vm_frame_push(vm_t *vm, frame_t *frame) { stack_push(vm->frames, frame); }

frame_t *vm_new_frame(vm_t *vm) {
        frame_t *frame = malloc(sizeof(frame_t));
        frame->references = stack_new(8);

        vm_frame_push(vm, frame);
        return frame;
}

void frame_free(frame_t *frame) {
        stack_free(frame->references);
        free(frame);
}
