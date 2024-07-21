"""
write a function which takes a potentially
deeply nested list of lists, and returns (or prints)
one with an appropriate amount of indentation at each level.
as a stretch goal, support multiple nested types, 
e.g both lists and dictionaries, or a whole JSON object

plan:
    - if element is not a list,
    print it with a comma
    - if first element, print a open square bracket
    - if last element, print a close square bracket
    - if it is a list, 
    do the above


"""

l = [1, 2, 3, ["a", "b", ["c"], "foo"], 4]
simplelist = [1, 2, 3, 4, [5, 6]]
k = [1, 2, 3, 4, 5, 6]


def fmt(lst, depth=1):
    """
    given a list of lists, return a formatted string with correct indentation
    """
    parts = []
    for x in lst:
        parts.append(fmt(x, depth + 1) if type(x) is list else repr(x))
    return "[" + (",\n" + " " * depth).join(parts) + "]"


if __name__ == "__main__":
    # print(pretty(l))
    print(fmt(l))
    # print(fmt(simplelist))
    # print(fmt([1, 2, 3]))
    # (pretty(k))
    # assert fmt([]) == "[]"
    # assert fmt([1, 2, 3]) == "[1,\n 2,\n 3]"

    print("ok")
