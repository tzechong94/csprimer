def exp_recursive(a, n):
    """
    a*a... n times
    """
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        return exp_recursive(a * a, n / 2)
    else:
        return a * exp_recursive(a, n - 1)


def exp_iterative(a, n, acc):
    if n == 0:
        return acc
    if n == 1:
        return a
    if n // 2 == 0:
        return exp_iterative(a * a, n % 2, acc)
    else:
        return exp_iterative(a, n - 1, a * acc)


def exp(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return a * exp(a, n - 1)

    res = exp(a, n >> 1)
    return res * res


if __name__ == "__main__":
    cases = (
        (2, 10),
        (3, 10),
        (10, 10),
        (100, 10),
        (1000, 10),
        (10000, 10),
    )

    for base, power in cases:
        print(base, power, exp_recursive(base, power))

        assert exp_recursive(base, power) == base**power

    print("ok")
