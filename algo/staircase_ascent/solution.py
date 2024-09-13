# staircase of n steps, can go up 1,2,3 steps at a time. how many different ways?

# plan
# sounds similar to the change making coin problem.
# base case, if amount is 0, there is exactly 1 way
# if amount is negative or no coins left, there is no way
# recursive case:
# 1. include the largest coin: subtract its value from the amount and solve for the remainer
# 2. exclude the largest coin: solve for the same amount using smaller coins


def staircase_ascent(n, list=[3, 2, 1]):
    if n == 0:
        return [[]]
    if n < 0 or len(list) == 0:
        return []
    permutations = []

    for step in list:
        remaining_permutations = staircase_ascent(n - step, list)

        for perm in remaining_permutations:
            permutations.append([step] + perm)

    return permutations


list = [3, 2, 1]
print(len(staircase_ascent(1, list)))
print(len(staircase_ascent(2, list)))
print(len(staircase_ascent(3, list)))
print(len(staircase_ascent(4, list)))
print(len(staircase_ascent(5, list)))

# fibonacci, use caching


def f(n):
    if n <= 2:
        return (1, 1, 2)[n]
    return f(n - 1) + f(n - 2) + f(n - 3)


def f2(n):
    a, b, c = 1, 1, 2
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a


if __name__ == "__main__":
    expectations = (1, 1, 2, 4, 7, 13)
    for i, x in enumerate(expectations):
        assert f(i) == x
        assert f2(i) == x
    print("ok")
