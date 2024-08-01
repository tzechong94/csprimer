/*
no inheritance, otherwise basic idea same as class
*/

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define STARTING_CAPACITY 8

// 8 bytes for void pointer pointer, 4 byte for integer, 4 bytes for integer
typedef struct DA {
  // TODO define our struct
  void** items; // pointer to pointer to anything
  int length; // number of items in the dynamic array right now
  int capacity; // start at 8. will determine if need to grow again
  /*
  int *data;
  int size;
  int capacity;
  */
} DA;

// DA* declares a pointer to a DA struct
// DA *da declares a variable da that is a pointer to a DA struct
// *da is used to dereference the pointer da, allowing access to the struct it points to
// da->size is same as (*da).size, which access the size field of the struct that da points to
// Memory allocation
// malloc is a function that allocates a block of memory and returns a pointer to the beginning of this block. the size of the block is in bytes
// (DA *) casts pointer returned by malloc to the appropriate type, in this case a pointer to a DA struct
DA* DA_new (void) {
  // TODO allocate and return a new dynamic array
  DA *da = (DA *)malloc(sizeof(DA));
  da->length = 0;
  da->capacity = STARTING_CAPACITY;
  da->items = malloc(STARTING_CAPACITY * sizeof(void*));
  return da;
}


void DA_free(DA *da) {
  // TODO deallocate anything on the heap
  free(da->items);
  free(da);
}

// good practice to do allocation or dellocation around the same place so you dont forget

int DA_size(DA *da) {
  // TODO return the number of items in the dynamic array
  // return sizeof(*da);
  return da->length; // or (*da).length
}

void DA_push (DA* da, void* x) {
  if (da->length == da->capacity){
    da->capacity <<= 1;
    da->items = realloc(da->items, da->capacity * sizeof(void *)); // 8 void pointer
    printf("Resized to %d\n", da->capacity);
  }

  da->items[da->length++] = x;
}

// --da->length pre-decrement. decreases the value first by 1 before current value is used in the expression 
// da->length-- post decrement, decreases the value by 1 after current value has been used in expression
void *DA_pop(DA *da) {
  if (da->length == 0) return NULL;
  return da->items[--da->length];
  // --da->length changes the actual length of the struct, not just using it as an index
}

void DA_set(DA *da, void *x, int i) {
  // TODO check bounds. check below and outside of length
  if (i < 0 || i >= da->length){
    return -1;
  }
  da->items[i] = x;
}

void *DA_get(DA *da, int i) {
  // TODO check bounds
  if (i < 0 || i >= da->length){
    return NULL;
  }
  return da->items[i];
}



int main() {
    DA* da = DA_new();

    assert(DA_size(da) == 0);

    // basic push and pop test
    int x = 5;
    float y = 12.4;
    DA_push(da, &x);
    DA_push(da, &y);
    assert(DA_size(da) == 2);

    assert(DA_pop(da) == &y);
    assert(DA_size(da) == 1);

    assert(DA_pop(da) == &x);
    assert(DA_size(da) == 0);
    assert(DA_pop(da) == NULL);

    // basic set/get test
    DA_push(da, &x);
    DA_set(da, &y, 0);
    assert(DA_get(da, 0) == &y);
    DA_pop(da);
    assert(DA_size(da) == 0);

    // expansion test
    DA *da2 = DA_new(); // use another DA to show it doesn't get overriden
    DA_push(da2, &x);
    int i, n = 100 * STARTING_CAPACITY, arr[n];
    for (i = 0; i < n; i++) {
      arr[i] = i;
      DA_push(da, &arr[i]);
    }
    assert(DA_size(da) == n);
    for (i = 0; i < n; i++) {
      assert(DA_get(da, i) == &arr[i]);
    }
    for (; n; n--)
      DA_pop(da);
    assert(DA_size(da) == 0);
    assert(DA_pop(da2) == &x); // this will fail if da doesn't expand

    DA_free(da);
    DA_free(da2);
    printf("OK\n");
}
