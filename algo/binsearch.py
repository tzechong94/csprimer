import random
import timeit
import matplotlib.pyplot as plt


def binsearch(nums, n):
    lo, hi = 0, len(nums)
    while hi > lo:
        mid = (lo + hi) // 2  # still in range [lo, hi)
        x = nums[mid]
        if x == n:
            return mid
        if n < x:
            hi = mid
        if n > x:
            lo = mid + 1
    return None


def itersearch(nums, n):
    for i, x in enumerate(nums):
        if x == n:
            return i
    return None


sizes = [
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800,
    900,
    1000,
    1100,
    1200,
    1300,
    1400,
    1500,
    1600,
    1700,
    1800,
    1900,
    2000,
]

binsearch_times = []
linsearch_times = []
for size in sizes:
    nums = sorted(random.sample(range(2000), size))
    target = random.choice(nums)

    binsearch_time = timeit.timeit(lambda: binsearch(nums, target), number=1000)
    linsearch_time = timeit.timeit(lambda: itersearch(nums, target), number=1000)
    binsearch_times.append(binsearch_time)
    linsearch_times.append(linsearch_time)

plt.plot(sizes, binsearch_times, label="Binary Search")
plt.plot(sizes, linsearch_times, label="Linear Search")
plt.xlabel("Array Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Search Algorithm Performance")
plt.legend()
plt.show()
# if __name__ == "__main__":
#     a = (0, 1, 3, 4)
#     b = (-5, -2, 0)
#     cases = (
#         # find in any position, even size
#         (a, 0, 0),
#         (a, 1, 1),
#         (a, 3, 2),
#         (a, 4, 3),
#         # find in any position, odd size
#         (b, -5, 0),
#         (b, -2, 1),
#         (b, 0, 2),
#         # fail to find
#         (a, 2, None),
#         (b, -3, None),
#     )
#     for nums, n, exp in cases:
#         assert binsearch(nums, n) == exp
#     print("ok")
