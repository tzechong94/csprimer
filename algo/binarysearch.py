# if number in array -> return the index
# if number is not in the array, return false


from random import randint
import timeit
from matplotlib import pyplot


def binsearch(arr, n):
    # base case: if array len is 0, returns false
    # if array len is 1 && element is not n, returns false
    # if array len is more than 1, pick n/2 and use it as index. if n == element return index,
    # if n > element, split the array and do binary search on greater partition,
    # if smaller do on smaller partition
    # use // to get middle index
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == n:

            return mid

        elif n > mid_value:
            low = mid + 1
        else:
            high = mid - 1

    return None


def itersearch(nums, n):
    for i, x in enumerate(nums):
        if n == x:
            return i
    return None


if __name__ == "__main__":
    sizes = range(200)
    bintiming, itertiming = [], []
    for size in sizes:
        nums = sorted(randint(0, 10000) for _ in range(size))  # [0,size]
        bintiming.append(timeit.timeit(lambda: binsearch(nums, 42), number=3))
        itertiming.append(timeit.timeit(lambda: itersearch(nums, 42), number=3))

    pyplot.plot(sizes, bintiming, itertiming)
    pyplot.show()
