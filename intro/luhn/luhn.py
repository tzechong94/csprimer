"""
Now:

- write a function verify(digits) -> true/false, which validates a string of digit characters according to Luhn algorithm
- the final digit will be check digit: iterate through others in reverse order,
doubling each second digit (starting from rightmost non-check digit), adding together the resulting digits, combining to compute a total, which should be 10 - checkdigit mod 10
- testing strategy: verify(17893729974) -> True, verify(17893729975) -> False
- stick to simple imperative style (step by step)

Later:

- don't assume input is well formed, add extra tests to cover
- general refactor
- consider functional formulation
- lookup table / pre caching

"""


def model_answer(digits):
    total = 0
    for i, d in enumerate(reversed(digits)):
        # if i % 2 == 0 -> 1 (if loop over everything including check digit)
        # if i % 2 == 1 -> 2 (including check digit)
        # if i % 2 == 0:
        #     multiplier = 2
        # else:
        #     multiplier = 1
        # x = int(d) * (2 - i % 2)
        x = int(d) * (1 + i % 2)
        # total += x // 10 + x % 10  # finds the sum of the digits
        total += x // 10 + x
        # avoid conditional logic
    # return 10 - (total % 10) == int(digits[-1])
    # return (int(digits[-1]) + total) % 10 == 0  # adds up to 60
    return total % 10 == 0  # with check digit in the beginning


def verify(digits):
    total_sum = 0
    check_digit = digits[-1]
    for index, d in enumerate(reversed(digits[:-1])):  # TODO ideally avoid slice
        sum_of_digit = 0
        # print(d, ": index", index)
        if index % 2 == 0:
            # print("even")
            d = int(d) * 2
            # print("d: ", d)
            if len(str(d)) > 1:
                for digit in str(d):
                    sum_of_digit += int(digit)
                    # print("digit: ", digit)
            else:
                sum_of_digit = d
        else:
            # print("odd")
            sum_of_digit = d
        total_sum += int(sum_of_digit)
        # print("total sum", total_sum)
    tabulated_check_digit = 10 - total_sum % 10
    # print(tabulated_check_digit, "tabulated")
    return check_digit == str(tabulated_check_digit)


def refactor1(digits):
    total = 0
    # check_digit = digits[-1]
    for index, d in enumerate(reversed(digits)):  # TODO ideally avoid slice
        x = d * (1 + index % 2)
        total += x // 10 + x
    return total % 10 == 0


def f(i, d):
    # i, d = args
    x = int(d) * (1 + i % 2)
    return x // 10 + x


def verify_functional(digits):
    total = sum(map(f, enumerate(reversed(digits))))
    return total % 10 == 0


def verify_functional2(digits):
    # list comprehension. can have filter functionality to, add if at the end. can map and filter
    return sum([f(i, d) for i, d in enumerate(reversed(digits))]) % 10
    # the difference below is no list is created
    return sum(f(i, d) for i, d in enumerate(reversed(digits))) % 10


LOOKUP = (
    dict(zip("0123456789", (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))),
    dict(zip("0123456789", (0, 2, 4, 6, 8, 1, 3, 5, 7, 9))),
)


def f2(index, digit):
    LOOKUP[index % 2][digit]


def lookup_table(digits):
    total = 0
    # print(LOOKUP)
    for index, digit in enumerate(reversed(digits)):
        total += LOOKUP[index % 2][digit]
    return total % 10 == 0


if (
    __name__ == "__main__"
):  # this checks is the script is run directly, not imported. if imported, the lines below wont run
    # assert verify("17893729974")
    # assert not verify("17893729975")
    # assert model_answer("17893729974")
    # assert not model_answer("17893729975")
    # assert refactor("17893729974")
    # try:
    assert lookup_table("17893729974")
    assert not lookup_table("17893729975")
    # except KeyError:

    print("ok done")
