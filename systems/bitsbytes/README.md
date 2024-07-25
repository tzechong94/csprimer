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

### What is standard in and standard out

### canonical mode on terminal 

- wait till enter is pressed before input is sent to program
  
### flush a buffer

taking things off a buffer and putting it to wherever you want it to go. pushing things out of the buffer.

### file descriptor

- is our interface to the operating system specify which open file or file like thing we care about or working with.

Unix family operating systems use file descriptors 0, 1 and 2 to refer to standard in, standard out and standard error respectively, so that programs can be easily read from and write to a terminal interface, and be made to connect with one another via pipes.

0: stdin
1: stdout
2: stderr

eg.
curl -v example.com > /tmp/example -> write content to file, show verbose on terminal
curl -v example.com 2 > /tmp/example -> write verbose to file, show content on terminal

1 hexadecimal = 4 bits
1 byte = 8 bits = 2 hexadecimal


## BMP file format

- used to store bitmap digital images independently of the display devices
- capable of storing 2D digital images in various color depths, optionally with data compression, alpha channels and color profiles

a device independent bitmap (DIB) is a format used to define device-independent bitmaps in various color resolutions. The main purpose of DIBs is to allow bitmaps to be moved from one device to another. DIB is an external format, in contrast to a device dependent bitmap, which appears in the system as a bitmap object created by an application.

DIB is normally transported in metafiles, BMP files, and clipboard

#### File structure

- bitmap file header, mandatory, store general info
- DIB header, mandatory, store detailed info and define pixel format
- extra bit masks, optional, to define pixel format, present only in case DIB header is the BITMAPINFOHEADER and compression method member is set to either BI_BITFIELDS or BI_ALPHABITFIELDS
- color table, semi optional, define colors used by bitmap image data, mandatory for color depths <= 8 bits
- Gap1, optional, structure alignment, an artifact of file offset to pixel array in the bitmap file header
- pixel array, mandatory, define the actual values of the pixels, pixel format is defined by DIB header or extra bit masks, each row in the pixel array is padded to a multiple of 4 bytes in size
- gap2, optional, for structure alignment, artifact of icc profile data offset field in the dib header
- icc color profile, optional, define color profile for color management, can also contain a path to an external file containing the color profile, when loaded in memory as non packed DIB, it is located between color table and gap1

#### DIBs in memory

when loaded into memory, bitmap image file becomes dib data structure. does not contain 14-byte bitmap file header and begins with the DIB header.
pixel array must begin at memory address that is a multiple of 4 bytes. 

#### bitmap file header

used to identify a file, block of bytes at the start of the file. read this to ensure that the file is actually a BMP and it is not damaged. the first 2 bytes of the BMP file format are the character B and then the character M in ASCII encoding. all the integer values are stored in little-endian format. (least significant byte first)

- 00 offset, 2 bytes: BM in ASCII. 0X42 0X4D
- 02 offset, 4 bytes: the size of BMP file in bytes
- 06 offset, 2 bytes: reserved: actual value depends on application that created the image, if created manually can be 0
- 08 offset, 2 bytes: reserved actual value depends on the application that creates the image, if created manually can be 0
- 0A offset (10), 4 bytes: the offset, starting address, of the byte where the bitmap image data (pixel array can be found)

## Network protocol intro

TCP - transmission control protocol 

- TCP connection -> 3 way handshake.
- syn -> syn/ack -> ack
- sy flood: if attacker wants to send syn messages, server will send ack back, but if the attacker doesnt reply with the 3rd ack message, lots of server will be half opened.

### SYN Flood

syn flood is a form of dos attack on data communications in which an attacker rapidly initiates a connection to a server without finalizing the connection. server has to spend resources waiting for half opened connections, which can consume enough resources to make the system unresponsive to legitimate traffic

attacker sends a syn packet, part of TCPs three way handshake used to established a connection

#### details

1. client requests connection by sending a syn messge to server
2. server acknowledges this by sending syn-ack back to client
3. client responds with an ack, connection established

- not responding with the final ACK code, malicious client can either simply not send the expected ACK, or by spoofing the IP adress in the syn, causing the server to send syn-ack to a falsified IP address, which will not send an ACK because it doesn't know

- half open connections take up resources and server cannot connect to legit clients, or crash

#### Countermeasures

- filtering
- increasing backlog
- reducing syn-received timer
- recycling oldest half open TCP
- syn cache
- syn cookies
- hybrid approaches
- firewalls and proxies

#### PCAP File format

- pcap header
- per packet pcap header
- link layer header
- ip header
- tcp header
- 

1. Pcap header to confirm version #. parse magic number


#### Localhost -> loopback interface

- work with virtual network interface locally that is very similar to sending something out of the physical network, but instead all it does is reflects back from inside of the operating system's TCP/IP. 
- message is addressed to localhost as hostname or the IP address, goes into network of OS, not going out through a network card, just mimicking a real network