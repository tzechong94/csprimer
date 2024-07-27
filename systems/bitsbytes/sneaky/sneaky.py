# 1 sign bit, 11 exponent bit, 4 bit for length, 48 bits message
import struct


def conceal(msg):
    # 64 bit is 8 bytes
    # nan = 0b011111111111
    # strlen = len(str)
    # print(nan, bin(strlen)[2:])

    # str_in_bytes = struct.unpack(">IIIIII", (str))[0]

    bs = msg.encode("utf8")
    n = len(bs)
    if n > 6:
        raise ValueError()
    first = b"\x7f"
    second = (0xF8 ^ n).to_bytes(1, "big")  # ^ is xor
    padding = b"\x00" * (6 - n)
    payload = bs
    return struct.unpack(">d", first + second + padding + payload)[0]
    # converts a bytes object (binary data) back into python 
    # values based on a specified format string

def extract(x):
    # first 4 bytes, i only want the last 3 bits

    bs = struct.pack(">d", x) # converts python values into a bytes object (binary data) 
    # based on the specified format string
    print(bs)
    n = bs[1] & 0x07
    return bs[-n:].decode("utf8")


if __name__ == "__main__":
    case = "secret"
    x = conceal(case)
    assert isinstance(x, float)
    assert repr(x) == "nan"
    print(x)
    print(x.hex())
    print(extract(x))
    assert extract(x) == case
