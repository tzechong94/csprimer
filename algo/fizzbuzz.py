import time


def fizzbuzz_sum_constant(n):
    # n // 15 = a
    # n // 5 = b
    # n // 3 = c
    # triangular number = n*(n+1)/2
    # sum = 5*triangular + 3*triangular - 15*triangular
    a = (n - 1) // 15
    # print("a", a)
    b = (n - 1) // 5
    # print("b", b)
    c = (n - 1) // 3
    # print("c", c)
    triangular_a = triangular(a)
    # print("triangular_a", triangular_a)
    triangular_b = triangular(b)
    # print("triangular_b", triangular_b)
    triangular_c = triangular(c)
    # print("triangular_c", triangular_c)
    return 5 * triangular_b + 3 * triangular_c - 15 * triangular_a


def triangular(n):
    return n * (n + 1) // 2


def fizzbuzz_sum_linear(n):
    sum = 0
    for i in range(1, n):
        if i % 5 == 0 and i % 3 != 0:
            sum += i
        if i % 3 == 0:
            sum += i
    return sum


def time_function(func, arg):
    start_time = time.time()  # Record start time
    result = func(arg)  # Call the function
    end_time = time.time()  # Record end time
    time_taken = end_time - start_time  # Calculate the time taken
    print(f"Result: {result}, Time taken: {time_taken} seconds")
    return result, time_taken


# Measure time for each function call
print("Timing fizzbuzz_sum_constant(10)")
time_function(fizzbuzz_sum_constant, 5000)

print("Timing fizzbuzz_sum_constant(1000)")
time_function(fizzbuzz_sum_constant, 1000)

print("Timing fizzbuzz_sum_linear(10)")
time_function(fizzbuzz_sum_linear, 5000)

print("Timing fizzbuzz_sum_linear(1000)")
time_function(fizzbuzz_sum_linear, 1000)
