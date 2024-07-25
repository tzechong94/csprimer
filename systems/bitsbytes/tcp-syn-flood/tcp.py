"""
parse the file with code,
figure out what percentage of SYN package
were ACKed, what was the server actually
able to acknowledge
- figure what the flags are
- what messages are
- what percentage of initiated connection is acknowledged

1. parse pcap header: confirm version
2. parse per packet headers
3. parse link layer header (loopback 4 bytes)
4. parse IP header (at least the length)
5. parse TCP header (syn and ack flags)

network protocols use big endian
pcap uses little endian (pcap header and per packet)
"""


def le(bs):
    n = 0
    for i, b in enumerate(bs):
        n += b << (i * 8)
    print(n)
    return n


with open("synflood.pcap", "rb") as f:
    data = f.read()

magic_number = le(data[0:4])
major_version = le(data[4:6])
minor_version = le(data[6:8])
pcap_header = le(data[0:24])

print("pcap_header:", hex(pcap_header))
print("magic number:", hex(magic_number))
print("major_version:", hex(major_version))
print("minor_version:", hex(minor_version))
