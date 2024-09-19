# if number in array -> return the index
# if number is not in the array, return false


def binary_search(n, arr):
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
            print("low: ", low, "high: ", high, "mid: ", mid)
            print("Found")
            return mid

        elif n > mid_value:
            print("low: ", low, "high: ", high, "mid: ", mid)
            low = mid + 1
        else:
            print("low: ", low, "high: ", high, "mid: ", mid)
            high = mid - 1

    return False


# def binsearch(nums, n):
#     """
#     let lo, high, be 0 and len(nums)... then we know, if n is
#     in nums, then it must be in [lo,hi]
#     while hi > lo:

#         mid = (lo + hi)//2
#         x = nums[mid]
#         if x == n:
#             return mid
#         if n < x:
#             hi = mid
#         if n > x:
#             lo = mid + 1

#     """
#     pass


if __name__ == "__main__":
    array = [
        103,
        191,
        217,
        227,
        253,
        337,
        340,
        394,
        417,
        507,
        533,
        560,
        608,
        621,
        716,
        764,
        771,
        833,
        865,
        923,
    ]
    for i, x in enumerate(array):
        assert binary_search(x, array) == i

    # assert binary_search(5, array) == False
    # assert binary_search(-5, array) == False

    # a = (0, 1, 3, 4)
    # b = (-5, -2, 0)
    # cases = (
    #     (a, 0, 0),
    #     (a, 1, 1),
    #     (a, 3, 2),
    #     (a, 4, 3),
    #     (b, -5, 0),
    #     (b, -2, 1),
    #     (b, 0, 2),
    #     (a, 2, None),
    #     (b, -3, None),
    # )
    # for nums, n, exp in cases:
    #     assert binsearch(nums, n) == exp

    print("ok")
