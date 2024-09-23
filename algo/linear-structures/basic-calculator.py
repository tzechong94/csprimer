# def calculator1(s):
#     """
#     s = []
#     for ch in expr:
#         if digit: push to stack
#         if op: push function corresponding to op
#         if ')':
#             pop last 3 values from stack, and evaluate operator function with two arguments
#         else:
#             continue
#     return s.pop()
#     """
#     operators = "+-*/"
#     stack = []
#     operations = {
#         "+": lambda x, y: x + y,
#         "-": lambda x, y: x - y,
#         "*": lambda x, y: x * y,
#         "/": lambda x, y: x / y,
#     }

#     for ch in s:
#         if ch != "(" and ch != ")":
#             stack.append((ch))
#         elif ch == ")":
#             val2 = stack.pop()
#             op = stack.pop()
#             val1 = stack.pop()
#             answer = operations.get(op)(int(val1), int(val2))
#             stack.append(answer)
#     val2 = stack.pop()
#     op = stack.pop()
#     val1 = stack.pop()
#     answer = operations.get(op)(int(val1), int(val2))
#     return answer

OPS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}


class InvalidExpression(ValueError):
    pass


def calculator(expr):
    s = []
    for ch in expr:
        if ch.isdigit():
            if len(s) == 0 or not isinstance(s[-1], int):
                s.append(int(ch))
            else:
                s[-1] = s[-1] * 10 + int(ch)
        elif ch in OPS:
            s.append(OPS[ch])
        elif ch == ")":
            try:
                b, op, a = s.pop(), s.pop(), s.pop()  # TODO what if stack is empty
            except IndexError:
                raise IndexError()
            s.append(op(a, b))
    if len(s) != 1:
        raise InvalidExpression()
    return s.pop()


if __name__ == "__main__":
    input = "(2+3)*5"  # answer = 25
    # assert calculator(input) == 25
    print(calculator(input))
    input = "(1+2)*3"  # answer = 9
    # assert calculator(input) == 9
    print(calculator(input))

    input = "(1-(2-3)+7)"  # answer = 9
    # assert calculator(input) == 9
    print(calculator(input))

    print("ok")
