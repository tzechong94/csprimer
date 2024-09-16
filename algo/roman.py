def integer_to_roman(num: int):
    if not isinstance(num, int):
        raise ValueError("Input must be integer")
    if num <= 0:
        raise ValueError("Input cannot be negative or 0")

    if num >= 1000:
        return "M" + integer_to_roman(num - 1000)
    if num >= 900:
        return "CM" + integer_to_roman(num - 900)
    if num >= 500:
        return "D" + integer_to_roman(num - 500)
    if num >= 400:
        return "CD" + integer_to_roman(num - 400)
    if num >= 100:
        return "C" + integer_to_roman(num - 100)
    if num >= 90:
        return "XC" + integer_to_roman(num - 90)
    if num >= 50:
        return "L" + integer_to_roman(num - 50)
    if num >= 40:
        return "XL" + integer_to_roman(num - 40)
    if num >= 10:
        return "X" + integer_to_roman(num - 10)
    if num >= 9:
        return "IX" + integer_to_roman(num - 9)
    if num >= 5:
        return "V" + integer_to_roman(num - 5)
    if num >= 1:
        return "I" + integer_to_roman(num - 1)
    return ""


parts = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (1, "I"),
)


# recursive
def f(n):
    for d, r in parts:
        if n <= d:
            return r + f(n - d)
    return ""


# iterative
def f_iter(n):
    result = ""
    for d, r in parts:
        while n <= d:
            result += r
            n -= d
    return result


# or create a map of all decimal places, then divide to find the multiple, and add the strings tgt
