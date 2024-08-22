#include <assert.h>
#include <stdio.h>

extern int sum_to_n(int n);


int main(void) {

  assert(sum_to_n(0) == 0);
  printf("0 OK\n");

  assert(sum_to_n(1) == 1);
  printf("1 OK\n");

  assert(sum_to_n(3) == 6);
  printf("3 OK\n");

  assert(sum_to_n(10) == 55);
  printf("55 OK\n");

  assert(sum_to_n(1000) == 500500);
  printf("1000 OK\n");

  printf("ALL OK\n");
}
