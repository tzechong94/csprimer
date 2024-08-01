#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// bitset
// if it's not a-z, ignore
// if it's not lower case, make it lower case
// bs |= 1 << (ch - f'a)
// return bs == 0x03ffffff
// A-Z = 65 to 90
// a-z = 97 to 122

#define MASK 0x07fffffe

bool ispangram(char *s) {
  // TODO implement this!
  
  // uint32_t bs = 0;
  // char c;
  // while (*s != '\0') {
  //   c = tolower(*s++); // or s++ separately
  //   if (c < 'a' || c > 'z') continue;
  //   bs |= 1 << (c - 'a');

  // }
  // return bs == 0x03ffffff;

  // using the ascii table. first bit is @, last few bit is other symbols
  // with this method you just use the ascii value directly without minusing the limits of the alphabets, hence the mask
  uint32_t bs = 0;
  char c;

  while ( (c = *s++) != '\0') { // *s++ fetches current character, and advances the pointer to next charcter in the string
    if (c < '@') continue; // ignorefirst 64 chars in ascii table
    bs |= 1 << (c & 0x1f);
  }
  return (bs & MASK) == MASK;
     

}

int main() {
  size_t len;
  ssize_t read;
  char *line = NULL;
  while ((read = getline(&line, &len, stdin)) != -1) {
    if (ispangram(line))
      printf("%s", line);
  }

  if (ferror(stdin))
    fprintf(stderr, "Error reading from stdin");

  free(line);
  fprintf(stderr, "ok\n");
}
