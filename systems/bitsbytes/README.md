# notes

python implements numbers in a way where it stores an array of integers which are effectively the parts of your large number

adding parts together when overflow

## Encoding

### Base 128 Varints

variable width integers or varints are at the core of wire format. Allow encoding unsigned 64 bit integers using anywhere between 1 to 10 bytes, with small values using fewer bytes.

Each byte in the varint has a continuation bit that indicates if byte follows it is part of the varint. This is the most significant bit (on the left most), lower 7 bits are payload. Resulting integer is built by appending together the 7 bit payloads of its constituent bytes.

0000 0001 -> `01` backticks denote raw hex literal
10010110 00000001 -> 150 encoded as `9601`

how to know that's 150?

1. Drop continuation bits
   1. 0010110 0000001
2. Convert to big endian
   1. 0000001 0010110
3. Concatenate
   1. 00000010010110
4. interpret as unsigned 64 bit integer
   1. 128 + 16 + 4 + 2 = 150

### Message structure

Protocol buffer message is a series of key-value pairs. Binary version of the message just uses the field's number as the key - the name and declared type for each field can only be dtermined on the decoding end by referencing the message type's definition

protoscope does not have access to this information, so it can only provide the field numbers

when message is encoded, each key-value pair is turned into a record consisting of the field number, a wire type and a payload. Wire type tells parser how big the payload after it is. Allows old parsers to skip over new fields they don't understand. --> called tag length value or TLV

6 wire types: VARINT, I64, LEN, SGROUP, EGROUP, I32

'tag' of a record is encoded a a varint formed from the field number and the wire type via the formula (field_number << 3) | wire_type

low 3 bits tell us the wire type, the rest of the integer tells us the field number

For example:
0000 1000
-> drop MSB
000 1000 -> `08`

take last 3 bits to get wire type 0
right shift by three to get field number 1
protoscope represents a tag as an integer followed by a colon and the wire type, so we can write the above bytes as 1:VARINT decoded-value

-> since wire type is 0, (varint), we need to decode varint to get the payload.

### struct

declare a binary data layout, provide a buffer, unpack values 

### What is bitwise shift?

can think of it as multiplying or dividing by 2^ number shifted

shift left << is multiplying
shift right >> is dividing

### why are some bitwise operations faster than arithmetic equivalent?

- think: how many CPU cycles would it take to complete a multiplication vs shift
- what is the throughput the CPU can execute sequence of independent instructions of that sort in the scenario where you're executing these in a loop

Agner Fog's tables

- reciprocal throughput -> instruction level parallelism, ie parallel execution on a single cpu core of multiple instructions for a single thread, not additional parallelism achieved by multi threading

### why does one byte correspond to two hex digits

4 bit = 16 possible thing -> 8 bit = use 2 hex digits

### Bitwise operations

and or xor xand not

### what are signed and unsigned integers?

are there just positive integers or are negative integers there too?

- eg signed scheme called two's complement
- 1111 is -1, think of it like -8 + 7, etc etc
