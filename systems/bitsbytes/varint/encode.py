"""
write a program that can encode 64-bit unsigned
integers into the protocol buffers varint encoding

10010110 00000001
1. Drop continuation bits
   1. 0010110 0000001
2. Convert to big endian
   1. 0000001 0010110
3. Concatenate
   1. 00000010010110
4. interpret as unsigned 64 bit integer
   1. 128 + 16 + 4 + 2 = 150

read the test files
    hexdump
    interpret as int
implement basic varint encoder
implement decoder
roundtrip test

"""

import struct


def encode(n):
    # convert to binary
    # check if continuation bit is 1
    # not 1, read first 7 bits and convert to hex bytes
    # if 1, add a 0000001 to the end and convert to hex bytes
    """
    while n > 0:
        take lowest order 7 bits
        add to correct msb: 1 unless final 7 bits
        push to some sequence of bytes
        reduce n by 7 bits
    return byte sequence
    0x80 = 1000 0000
    n += b & 0x7F  # mask

    """

    out = []
    while n > 0:  # TODO avoid double checking
        part = n & 0x7F  # mask away the msb, similar to modulo 128
        n >>= 7  # dividing by 128
        part |= n and 0x80 or 0x00  # add a msb 1 if n is more than 128
        out.append(part)
    return bytes(out)


def decode(varn):
    """
        10010110 00000001
    1. Drop continuation bits
       1. 0010110 0000001
    2. Convert to big endian
       1. 0000001 0010110
    3. Concatenate
       1. 00000010010110
    4. interpret as unsigned 64 bit integer
       1. 128 + 16 + 4 + 2 = 150
    for b in varn in reverse order:
        - shift accumulator left 7
        - discard msb
        - accumulate b
    """
    n = 0
    for b in reversed(varn):
        n <<= 7  # similar to multiplying by 128
        n += b & 0x7F  # mask the first digit, make it 0
    return n


if __name__ == "__main__":
    cases = (
        ("1.uint64", b"\x01"),
        ("150.uint64", b"\x96\x01"),
        ("maxint.uint64", b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01"),
    )

    for fname, expectation in cases:
        with open(fname, "rb") as f:
            n = struct.unpack(">Q", f.read())[0]
            assert encode(n) == expectation
            assert decode(encode(n)) == n
    print("ok")
