def quicksort(nums):
    left = []
    right = []
    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])

    return quicksort(left) + [pivot] + quicksort(right)


def qsort(nums):

    def _sort(lo, hi):
        """
        sort nums from [lo, hi],
        partition using lombuto scheme
        recurse on lower and higher sides
        """
        if hi <= lo:
            return

        m = lo
        for i in range(lo + 1, hi + 1):
            if nums[lo] > nums[i]:
                m += 1
                nums[m], nums[i] = nums[i], nums[m]

        nums[lo], nums[m] = nums[m], nums[lo]
        # recurse on lower and higher sides

        _sort(lo, m - 1)
        _sort(m + 1, hi)

    _sort(0, len(nums) - 1)


if __name__ == "__main__":
    cases = [3, 2, 1, 5, 6, 4], [2, 34, 45, 61, 1, 2, 0]

    for case in cases:
        # print(case)
        expected = sorted(case)
        print(case, "case")
        (qsort(case))
        print(expected, "expected")
        print(expected, case)
        assert case == expected

    print("ok")
