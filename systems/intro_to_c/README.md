# Intro to C

## types

int, char, short, long, double, float

- int and float depends on machine type, 16 or 32 bit etc
- sizes of these objects are also machine dependent.
- arrays, structures and unions of these basic types, pointers to them, and functions that return them etc

- %d specifies and integer argument
- %3.0f -> floating point is to be printed at lest three characters wide, with no decimal point and no fraction digits
- %6.1f -> floating point, at least 6 characters wide, with 1 digit after the decimal point.
- %o for octal, %x for hexadecimal, %c for character, %s for character string, adn %% for % itself

- #define line dfines a symbolic name or symbolic constant to be a particular string of characters. Thereafter, any occurrence of name will be replaced by the corresponding replacement text. The name has the same form as a variable name: a sequence of letter and digits that begins with a letter. i.e constants in other languages but it's not a variable. No semicolon at the end of constant definition

- return 0 -> 0 is success

int main(int argc, char** argsv) -> argc is argument count. at least 1, including the program's name
char** argv or char\* argv[] -> argument vector, it is an array of strings (character pointers), where each string is one of the command-line arguments. The first agument argv[0] is the name of the program itself

## what happens in the compilation pipeline

CALL - compile, assemble, link, load

main.c -> compile to assembly code main.cs -> assemble to machine code main.o -> link to a.out
math.c -> math.as -> math.o -> link to a.out

cc main.c math.c means compiling both files together
cc -c -> object file, individually

c = getchar() -> c is the next character of input
putchar(c) -> prints character everytime it's called

## word counting

## type definitions and literals in C

basic types:
char, int, float, double

qualifiers:
long int e = 20L -> long e = 20L; %ld -> formatting for long
short int f = 5 -> short f = 5;
long or short is machine dependent: short at least 16 bit, etc depends on the machine

unsigned int g;
unsigned short int h;
unsigned long int i;
unsigned char c; -> char are signed or unsigned by default is machine dependent, and this is a common cause of bugs.

#include <stdint.h>
int32_t l = 50;
uint32_t m = 30; etc

compiler knows which machine code to emit if you declare the specific type, otherwise it's machine dependent.

https://hyperpolyglot.org/c
https://learnxinyminutes.com/docs/c/

## what does it mean for a value to be a certain number of bits?

number of bits given to store a value. if not considered, will lead to overflow.

### what is a register

memory that resides on the CPU that stores values that are going to be operated over

register access being extremely fast fraction of a nanosecond compared to tens or thousands of nanoseconds of RAM. having a constraint number of register, and it has a specific width, 64 in this case.

The malloc() function allocates memory and leaves the memory uninitialized, whereas the calloc() function allocates memory and initializes all bits to zero.

### How do C compilers differ?

GCC part of GNU, Clang part of LLVM. https://aosabook.org/en/v1/llvm.html

### Generic pointer (void \*) in C

- work directly with the address irrespective of the type

### \* in c

1. can be used for multiplication
2. pointer declaration like:
   1. int \*p -> p is a pointer to an integer
   2. char \*str -> str is a pointer to a character
3. Deferencing a pointer, which means accessing the value stored at the memory address the pointer is pointing to:
   1. int x = 10;
   2. int \*p = &x; // p is a pointer to the address of x
   3. int y = \*p; // y is assigned the value at the memory address p points to
4. Pointer types in function parameters. \* is used to indicate that a parameter is a pointer to a specific type.

   void increment(int *num){
   (*num)++;
   }

int main() {
int a = 5;
increment(&a); // passing the address of a
printf("&d\n", a);
return 0;
}

### loop syntax

while,
do while ->
do {
printf("%d\n, n);
} while (n >0);
for (initialization; condition; increment). can be empty but semi colons have to be there.

### Overview of pointers and arrays in C

- memory: a bunch of cells from 0 to some large number.
- each of this is a byte, can reference them by number. memory is byte addressable.
- lets say integer stored at byte 40 - 43. (integer requires 4 byte.) int n = 5. it's an integer of 4 bytes stored at byte 40.
- inc(&n) -> increment the integer stored at byte40. doing inc(n) makes a copy.
- 

### -o flag in clang

optimization level flag
- optimization -> readability of disassembly 

### brief overview of structs in C. 

- something like objects without methods.


### basic hashmap

- "foo" -> hash uint 32 -> collapse down to some number of buckets -> 3
- have a finite number of buckets (eg 8), index 3 -> foo = 5.
- "bar" = 42 can be hashed to the same bucket too. collisions resolution -> chaining and open addressing
- chaining -> at each bucket location, instead of storing one thing, store the start of a linked list.
- open addressing -> as chains get longer, inefficient to traverse linked lists -> memory hierarchy -> cache miss.
- most hash table designs employ an imperfect hash fuction. Hash collision, where hash function enerates the same index for more than one key, therefore typically must be accommodated in some way.
- in a well-dimensioned hash table, the average time complexity for each lookup is independent of the number of elements stored in the table. 
- many hash table designs also allow arbitrary insertions and deletions of key value pairs, at amortized constant average cost per operation.
- Hashing is an example of space-time tradeoff. 
  - if memory infinite, the entire key can be used directly as an index to locate its value with a single memory access.
  - if infinite time is available, values can be stored without regard for their keys, and a binary search or linear search can be used to retrieve element.

#### Overview

an associative array stores a set of (key, value) pairs and allows insertion, deletion and lookup, with the constraint of unique keys.

- an array A of length m is partially filled with n elements, where m >= n.
- a value x gets stored at an index location A[h(x)], where h is a hash function, and h(x) < m.

### Hash function

- maps the universe U of keys to indices or slots withint the table, that is h(x) in 0, 1,... m-1 for x in U. Bit length of u is confined within the word size of a computer architecture.
- Hash function h is said to be perfect for a given set S if each element x in S maps to a different value. Can be created if all keys are known ahead of time.

### Hashing schemes

1. by division (most commonly used)

   - h(x) = x mod m, where M is the hash digest of x and m is the size of the table.
  
2. by multiplication

   - h(x) = m ((MA)) mod 1, where A is a real valued constant and m is the size of the table. use golden ratio although any A produces the hash function.

### Load factor

- load factor (a) = n / m, where n is the number of entries occupied in the hash table, and m is the number of buckets.
- high load factor leads to deterioration of performance of the hash table.
- with separate chaining hash tables, each slot of the bucket array stores a pointer to a list or array of data.
- value of a,max that gives best performance is typically between 1 and 3.
- 

### Choosing hash function

- uniform distribution of the hash values is a fundamental requirement of a hash function. 
- non-uniform increases number of collisions and the cost of resolving them.
- uniformity can be evaluated by pearson's chi squared test.
- distribution needs to be uniform only for table szes that occur in the application. in particular, if one uses dynamic resizing with the exact doubling and halving of the table size, hash function needs to be uniform only when the size is a power of two. Some other hashing algo prefer to have the size to be a prime number.

### Search algo

2 parts: first part is computing a hash function which transforms the search key into an array index. second is collision resolution.

#### separate chaining

- building a linked list with key-value pair for each search array index.
- 

#### open addressing

- hash function should avoid clustering, the mapping of two or more keys to consecutive slots.
- when a new entry has to be inserted, the buckets are examined, starting with the hased-to slot and proceeding in some probe sequence, until an unoccupied slot is found. when searching for an entry, the buckets are scanned in the same sequence, until either the target record is found, or an unused array slot is found, which indicates an unsuccessful search.
  - linear probing, quadratic, double hashing


segfault -> segmentation error. -> common cause -> operating over NULL, which is address zero, no permissions. 