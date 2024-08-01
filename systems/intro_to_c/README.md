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
char** argv or char* argv[] -> argument vector, it is an array of strings (character pointers), where each string is one of the command-line arguments. The first agument argv[0] is the name of the program itself

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
