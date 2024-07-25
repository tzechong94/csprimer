def little_endian(bs):
    n = 0
    print("bs", bs)
    print(type(bs), " type of bs")
    for i, b in enumerate(bs):
        n += b << (i * 8)
        print("n", n)
    return n


with open("teapot.bmp", "rb") as f:
    data = f.read()

print(data[:2].hex())  # read the first two, BM
offset = data[10]
print(offset)
print(data[offset : offset + 6])

assert data[:2] == b"BM"

offset, width, height = (
    little_endian(data[10:14]),
    little_endian(data[18:22]),
    little_endian(data[22:26]),
)

spixels = data[offset:]

pixels = []  # bgr triplets
# iterate in the expected order for rotated pixels
# look up corresponding source pixel, append to pixels
for ty in range(width):  # TODO what should these be for non-squares
    for tx in range(width):
        sy = tx
        sx = width - ty - 1
        n = offset + 3 * (sy * width + sx)
        pixels.append(data[n : n + 3])


# for i in range(0, len(image_data), width):
#     tpixels.append([image_data[i : i + width]])

print(width, height)
print(type((data[offset:])))


with open("out.bmp", "wb") as f:
    f.write(data[:offset])
    f.write(b"".join(pixels))
