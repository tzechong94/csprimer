#include <stdio.h>

// struct Box {
//     char* name;
//     void* value;
// };

// int main() {
//     struct Box b1 = { "foo", "box"};
//     int n = 5;
//     struct Box b2 = { "bar", &n };

//     printf("values are: %s and %d\n", (char*)b1.value, *(int*)b2.value);

// }

int main() {
    int n = 5;

    int *p = &n;

    int foo = *p;

    int arr[10];

    arr[3] = 42;

    printf("arr + 3 = %p, *(arr + 3) = %d\n", arr + 3, *(arr + 3));

    printf("arr = %p, arr + 1 = %p\n", arr, arr+1); // address and address of next byte

    printf("n = %d, &n = %p\n", foo, p); // pointers have a type
}

// array is a name for the starting location of a contiguous sequence of things of the same type