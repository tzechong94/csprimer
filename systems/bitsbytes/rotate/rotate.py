import sys
import struct


def rotate_clockwise(filepath):

    with open(filepath, "rb") as file:

        bmp_header = struct.unpack("<2sIHHI", file.read(14))
        print("bmp_header: ", bmp_header)
        image_data_offset = bmp_header[4]
        image_size_bytes = bmp_header[1]

        dib_header_size_data = file.read(4)  # returns as byte string
        dib_header_size = struct.unpack("<I", dib_header_size_data)[0]
        # 124 # unpack interpret bytes and convert them into tuple of values according to the format
        print("dib_header_size_data: ", dib_header_size_data)
        print("dib_header_size: ", dib_header_size)

        file.seek(-4, 1)
        full_dib_header_data = file.read(dib_header_size)

        print("full_dib_header_data ", full_dib_header_data)

        file.seek(image_data_offset)
        image_data_size = image_size_bytes - image_data_offset
        image_data = file.read()

        # print("image data size: ", image_data_size)
        # hex_string = "".join(f"{byte:02x}" for byte in image_data)
        # print(hex_string)


if __name__ == "__main__":
    rotate_clockwise("rotated.bmp")
