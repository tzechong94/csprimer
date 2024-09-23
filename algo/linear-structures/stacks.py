"""
write a function which validates
a string of [], {} and () characters
to ensure they are correctly nested
"""


def stacks_brackets2(s):
    stack = []
    if len(s) % 2 != 0:
        return False
    for c in s:
        if c in "([{":
            stack.insert(0, c)
        elif c in ")]}":
            if not stack:
                return False
            if c == ")" and stack[0] != "(":
                return False
            if c == "]" and stack[0] != "[":
                return False
            if c == "}" and stack[0] != "{":
                return False
            else:
                stack.pop(0)
    return True


def stacks_brackets(s):
    complement = {"(": ")", "[": "]", "{": "}"}

    stack = []
    if len(s) % 2 != 0:
        return False
    for c in s:
        if c in "([{":
            stack.insert(0, c)
        elif c in ")]}":
            if not stack:
                return False
            if c != complement[stack[0]]:
                return False
            else:
                stack.pop(0)
    return True


MATCHES = {"(": ")", "[": "]", "{": "}"}
LEFT = set(MATCHES.keys())
RIGHT = set(MATCHES.values())


def is_balanced(chars):
    s = []  # stack of left hand chars
    for c in chars:
        if c in LEFT:
            s.append(c)
            continue
        if c not in RIGHT:
            continue
        try:
            prior = s.pop()
        except IndexError:
            return False  # right imbalance
        if MATCHES[prior] != c:
            return False  # mismatch
    return len(s) == 0  # false if left imbalance


if __name__ == "__main__":
    s = "({[()]}[])"
    assert stacks_brackets(s) == True

    s = "({[()]}[)"
    assert stacks_brackets(s) == False

    s = "({[()]}[]])"
    assert stacks_brackets(s) == False
    s = "({[()]}[]))"
    assert stacks_brackets(s) == False

    s = "({[()]}[])"
    assert stacks_brackets(s) == True
    s = "("
    assert stacks_brackets(s) == False
    print("ok")
