typedef enum snek_object_kind {
  INTEGER,
} snek_object_kind_t;

typedef union snek_object_data {
  int v_int;
} snek_object_data_t;

typedef struct snek_object {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;
