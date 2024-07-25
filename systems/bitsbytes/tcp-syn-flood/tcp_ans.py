import struct

with open("synflood.pcap", "rb") as f:
    magic_number, major, minor, _, _, _, llh_type = struct.unpack(
        "<IHHIIII", f.read(24)
    )

    assert magic_number == 0xA1B2C3D4  # confirm file is LE
    print(f"Pcap protocol version {major}.{minor}")
    assert llh_type == 0  # link layer header type
    print(
        "link layer header type: ", llh_type
    )  # https://www.tcpdump.org/linktypes.html
    """
    BSD loopback encapsulation, the link layer header is a 4 byte field in host byte order
    contains value 2 for ipv4, 24, 28 or 30 for ipv6 etc
    """
    count = 0
    initiated = 0
    acked = 0
    while True:
        per_packet_header = f.read(16)
        if len(per_packet_header) == 0:
            break
        count += 1

        _, _, length, untrunc_length = struct.unpack("<IIII", per_packet_header)
        assert length == untrunc_length
        packet = f.read(length)

        assert struct.unpack("<I", packet[:4])[0] == 2

        ihl = (packet[4] & 0x0F) << 2
        print("ihl: ", ihl)
        assert ihl == 20  # can skip ip header -  20 bytes
        # print("ip_type: ", struct.unpack("<I", packet[:4])[0])

        src, dst, _, _, flags = struct.unpack("!HHIIH", packet[24:38])

        syn = (flags & 0x0002) > 0
        ack = (flags & 0x0010) > 0
        if dst == 80 and syn:
            initiated += 1
        if src == 80 and ack:
            acked += 1
        print(f"{src} -> {dst}{syn and  'SYN' or ''}{ack and ' ACK' or ''}")

    print(
        f"{count} packets parsed {initiated} connection, {acked} ",
        f"{acked/float(initiated):0.2f} % acked",
    )
    print(f"{count} packets parsed")
