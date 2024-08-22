# Some assembly required

- CPU instruction cycle
  - fetch data from memory -> memory, also known as RAM, is a short term storage your computer has.
    - if CPU is a warehouse, accessing data is like going storage rack with boxes. each box (data) has a location (memory address).can claer contents at that memory address, or put new stuff in the box (store new pieces of data at that memory address)
  - decode that data to understand the instruction
  - execute the instruction

## Fetch

data is stored in the form of electricity (for short term memory), when power is off, short term storage gets cleared out.

cpu's registers are like small pigeonholes to move smaller packages, can access them faster than memory.

cpu can only do one thing at a time, put number down and grab the next number, stores first number into register for the time being.

limited space in registers. memory can hold 15 million times that amount. when we dont need to actively use those data for instruction we place in memory.

## Decode

computer can only read numbers. represented in 5 broad categories

1. instruction opcodes (add)
2. numeric values (10)
3. letters ("M")
4. registers (rax)
5. memory address (0x12345678)

cpu has a set of instructions built physically into the chip. mapped instrction to number.

eg. 1 - add, 2 - subtract

## Execute

once decoded, can execute. extra stpo at the arithmetic logic unit (ALU) if the instruction is arithmetic.

modern CPUs can simultaneously fetch, decode, and execute different instructions at the same time.

## Buses

- like conveyor belt in a warehouse.
- group of wires that allows electricity (and therefore information represented by 0s and 1s) to travel from one place to another, and there are different types of wires depending on what kind of data you want to send around
- electrical signals (data) travel around CPU on buses, reaches different parts of CPU, may have its value checked or modified.

## Processor Clock

- wanna make sure everything happens at a organised pace, no disruptions at stations.
- set everything to a timer. boxes move forward at a pace of 1 station per second, each station takes 1 second to perform its task.
- processor clock -> like a metronome. made of material that oscillates at a certain frequency, giving you a bunch of vibrations per second. each vibration is called a clock tick. keeps CPU in sync, signals CPU starts a new instruction by fetching instruction data from memory.
- important coz each clock tick, cpu reads one instruction. todays cpu are in gigahertz -> 1 bil cycles per second

## Assembly languages

- x86 most useful, more complciated to write. intel processors
- ARM used by most smartphones, apple m1 processors.
- z80 used by ti-8x calculators
- 6502 used by older systems
- risc-v used for educational purposes, simpler.
- game engines and other highly efficiency sensitive apps need to be optimized with assembly language

## Data

1 unit of data is a bit. 0 or 1.
8 bits is byte. why 8?

- when representing a single character, takes 8 bits to represent that character in data.
- use a table mapping which number represents which letter. done with ASCII Table

## Registers

- can think of registers as variables of assembly language. use a variable to store data for later use.
- first 6 general purpose, but some instructions may auto read or set them
- rax -> accumulator
- rbx -> base
- rcx -> counter
- rdx -> data
- rdi -> destination
- rsi -> source
- r8-r15 general purpose
- rbp -> stack base pointer
- rsp -> stack pointer
- rip -> instruction pointer
- eflags -> status/condition
  last 4 autoset.

### Register data

can only store numbers

- numbers, letters, memory addresses. stored as bits, amount of bits a register can hold depends on processor.
- 32-bit / 64-bit processors means the register size.
- words -> groups of bytes
  - single word is 2 bytes, 16 bits
  - double word is 4 bytes, 32 bits
  - quadruple word is 8 bytes, 64 bytes, also known as qword.

eg in js: let a = 5;

in assembly:
mov rax, 5;

setting value of a register, rax, to number 5.
mov is move. moves value on the right side into register on the left side.

mov rax, 1;
mov rax, 3;

adding 3 to 1.

mov rax, 3;
mov rbx, 1;
add rax, rbx;

sub is substract
mul is times

mov rax, 2;
mov rbx, 3;
mov rcx, 4;

mul rax, rbx;
add rax, rcx;

y = mx + c;

### Jumping for joy

- able to keep track which line of code it's executing because of the instruction pointer.
- also known as program counter
- instruction pointer stores memory address of the current line of the program it's executing, and updates itself automatically
- eg. each instruction is 8 bytes, each memory address represents a byte of data, each time an instruction finishes, the pointer adds 8 to itself
- we dont access instruction pointer directly.
  
can change where instruction pointer is pointing with a jump instruction.

mov rcx, 10
jmp .addNumbers
sub rcx, 11; // skip this line because jumping to add numbers


.addNumbers // this is a label.
  mov rax, 3
  mov rbx, 1
  add rax, rbx

### Conditionals

cmp rax, rbx // if rax < rbx then jump, else nothing
jl .jumpToHere.

cmp compares two values, records which one is greater or equal in a special register called eflags. 

jl -> jump if less than. jl checks eflags register. if eflags says that first argument to cmp was less than the second (rax < rbx), it jumps to the specified label. if rax >= rbx, it does nothing.

### Flags

- 5 flags on x86-64 processor
- zero flag : ZF
- after an operation, if the result is 0, ZF flag gets set to 1. If it's not 0, the flag gets set to 0.

### Loop de loop

mov rax, 8; exponent
mov rbx, 2; base
mov= rcx, 1; our result
mov rdx, 0; our counter

.calculatePower
  mul rcx rbx; multiply result by our base, save into rcx
  inc rdx; increment counter
  cmp rdx, rax; compare counter with exponent
  jl .calculatePower ; jump to beginning of loop if rdx < rax

### let's get functional

call .addNumbers
call .doSomethingElse

.addNumbers
  mov rax, 3
  add rax, 1
  ret

.doSomethingElse
  add rax, 1
  ret

call -> calling function, 
call is similar to jump, but it's actually doing multiple things underneath.

1. pushes what would have been the next instruction onto something called the stack
2. it then updates the instruction pointer to point at the memory addres of the first instruction inside of the .addNumbers label
  
ret -> return

- pop previous memory address off of the stack and into the instruction pointer

### How it all stacks up

Computers allocate a chunk of memory to be the stack, a place where you can store bytes for later use.

- push a value onto it, which goes on top of the previous values
- pop a value off of it, which removes it from the top of the stack and puts it in a register
- cannot get something from the bottom, needa go through the top
- LAST IN FIRST OUT

stack is accessed through a special register called the stack pointer %rsp, which keeps track of the memory address that points to the top of the stack. everytime you push onto the stack, it auto increments the pointer, if you pop, decrements it. 

stack is to store things for later. using stack is faster than using memory

stackoverflow -> stack running out of room eg loop that adds to stack

### How conventional

- how do i know what to choose and when?
  - every assembly language has its own set of conventions that dictate where a program expects things to be

- arguments get pushed on the stack to pass into the function
- arguments get popped off the stack and into registers to access inside of our function
- return values get saved in rax
- general purpose registers can be callee owned or caller owned

.fizz ; caller
  call .buzz ; callee

- if caller wants to use a caller owned register, it's able to do so freely
- if caller wants to use callee-owned register, they are responsible for savings its value by pushing it onto the staack before calling the callee. otherwise this register can be overridden by the callee, which will cause the caller to lose the value

- if callee wants to use a caller-owned reigster, they must first save its value by pushing it onto the stack
- before callee returns, they must restore the register to its original value by popping it off the stack and back into the regsiter
- callee can use a callee owned register

### Uppercaser

- rdi -> number of command line arguments that were passed. argc in c
- rsi -> array of the command line arguments that you typed in when you ran the program. argv[][] in c
- 
- rdi and rsi contain info about command line arguments. they are callee owned, which means any functions we call may messed with their values and not clean them up

let's keep their values safe by copying them into r12 and r13, which are caller owned registers. if assembly language etiquette is followed, if a function wants to use one of these, must first push its value onto the stack, then pop it back off into the register before returning.

## Tutorial

mov x, y 
and x, y
or x, y
xor x, y
add x, y
sub x, y
inc x
dec x
syscall n ; invoke operating system routine n
db ; a pseudo-instruction that declares bytes that will be in memory when the program runs

## Three kinds of operands

### Register operands

integer reigsters, flag register and xmm register

the 16 integer registers are 64 bits wide and are called r0 to r15

16 xmm reigsters, each 126 bits wide, xmm0 to xmm15


### Memory operands

these are the basic forms of addressing:

[ number ]
[ reg ]
[ reg + reg*scale ] scale is 1,2,4 or 8 only
[ reg + number ]
[ reg + reg*scale + number ]

number is called displacement, the plain register is called the base, register with the scale is called the index

[750]                  ; displacement only
[rbp]                  ; base register only
[rcx + rsi*4]          ; base + index * scale
[rbp + rdx]            ; scale is 1
[rbx - 8]              ; displacement is -8
[rax + rdi*8 + 500]    ; all four components
[rbx + counter]        ; uses the address of the variable 'counter' as the displacement

### immediate operands

200          ; decimal
0200         ; still decimal - the leading 0 does not make it octal
0200d        ; explicitly decimal - d suffix
0d200        ; also decimal - 0d prefex
0c8h         ; hex - h suffix, but leading 0 is required because c8h looks like a var
0xc8         ; hex - the classic 0x prefix
0hc8         ; hex - for some reason NASM likes 0h
310q         ; octal - q suffix
0q310        ; octal - 0q prefix
11001000b    ; binary - b suffix
0b1100_1000  ; binary - 0b prefix, and by the way, underscores are allowed

## linker stuff

ld hello.o -o hello -macosx_version_min 11.0 -L /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib -lSystem

[] when you're working with a memory address rather than the value stored in a register or a direct value. brackets tell the assembler that you want to access the memory at the address contained in a register, rather than using the value directly as an operand

- bracket means you are dealing with a memory location, not just a value. contains an address in memory, 