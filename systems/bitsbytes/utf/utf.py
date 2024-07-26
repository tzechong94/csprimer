import struct
import sys

"""
parse test cases
- read lines
- uint8 for n
- remember to strip trailing /n

truncation
- start from end
- if s[n] starts with 0b10, then n-=1
- remember to account for n out of bounds

finally
- print to stdout
- diff against expected
"""

# in UTF-8, characters can be 1 to 4 bytes long. The structure of the bytes in
# UTF-8 encoded character is such that:
# for single byte character, the byte is 0xxxxxxx, where x represents a bit
# for multibyte character, the first byte is 110xxxxx, 1110xxxx, or 11110xxx, indicating a 2,3,4 byte character respectively
# continuation bytes, which are part of a multibyte character, have a format 10xxxxxx

"""
1-byte (ASCII):

Format: 0xxxxxxx
Used for ASCII characters (U+0000 to U+007F).
2-byte sequence:

Format: 110xxxxx 10xxxxxx
Used for characters in the range U+0080 to U+07FF.
3-byte sequence:

Format: 1110xxxx 10xxxxxx 10xxxxxx
Used for characters in the range U+0800 to U+FFFF.
4-byte sequence:

Format: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Used for characters in the range U+10000 to U+10FFFF.

"""


def truncate(s, n):
    # if index longer than string, return full string
    if n >= len(s):
        return s
    # if index is more than 0 and
    # s[n] represents the current byte in the  sequence
    # 0xC0 is a hexidecimal representation of binary value 11000000w
    while n > 0 and (s[n] & 0xC0) == 0x80:
        n -= 1
    return s[:n]


# with open("cases", "rb") as f:
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#             break
#         # n = line[0] -> which byte to truncate
#         # s = line[1:-1] -> the line to truncate without the new line

#         sys.stdout.buffer.write(truncate(line[1:-1], line[0]) + b"\n")
