"""
write a program that converts the given css files to use rgb 
instead of hexadecimal color notation
"""

HEX_TABLE = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}


def hex_to_rgb(filepath):
    """
    for each line in file, look for #with digits
    convert hex to rgb decimal without libraries
    write to the same line same spot
        - the case doesn't matter
        - 0 to 255
        - 6 digit => rr gg bb
        - 8 digit => rr gg bb / alpha (opacity, which is hex / 255)
        - 3 digits => eg 123 => 112233, 0ab => 00aabb
        - 4 digits => similar to 3 digits. every digit repeats itself
    """

    def pair_conversion(hex_code):
        return HEX_TABLE[hex_code[0]] * 16 + HEX_TABLE[hex_code[1]]

    def return_rbg_string(hexstring):
        converted_red = pair_conversion(hexstring[0:2])
        converted_green = pair_conversion(hexstring[2:4])
        converted_blue = pair_conversion(hexstring[4:6])
        if len(hexstring) == 6:
            return f"rgb({converted_red} {converted_green} {converted_blue})"
        if len(hexstring) == 8:
            converted_alpha = int(pair_conversion(hexstring[6:8])) / 255
            return f"rgba({converted_red} {converted_green} {converted_blue} / {converted_alpha:.5f})"

    def convert(hex_code):
        newhexstring = hex_code[1:]
        if len(newhexstring) == 3:
            newhexstring = (
                newhexstring[0] * 2 + newhexstring[1] * 2 + newhexstring[2] * 2
            )
            return_rbg_string(newhexstring)
        elif len(newhexstring) == 4:
            newhexstring = (
                newhexstring[0] * 2
                + newhexstring[1] * 2
                + newhexstring[2] * 2
                + newhexstring[3] * 2
            )
            return_rbg_string(newhexstring)

        elif len(newhexstring) == 6 or 8:
            return_rbg_string(newhexstring)
        else:
            return hex_code

    with open(filepath, "r") as file:
        lines = file.readlines()
    modified_lines = []
    for line in lines:
        stripped_line = line.strip()
        index = stripped_line.find("#")
        if index == -1:
            modified_lines.append(line)
            continue
        color_code = stripped_line[index:-1]
        print("color_code", color_code)
        if color_code:
            new_rgb_code = convert(color_code.lower())
            modified_line = line.replace(color_code, new_rgb_code)
            modified_lines.append(modified_line)

    with open(filepath, "w") as file:
        file.writelines(modified_lines)


if __name__ == "__main__":
    (hex_to_rgb("simple.css"))
    # assert hex_to_rgb("simple.css") == "rgb(0, 255, 0)"
    print("ok")
