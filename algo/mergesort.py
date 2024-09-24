def mergesort1(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    mergesort(left)
    mergesort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


def mergesort(nums):
    working = [0] * len(nums)

    def merge(left, right, mid):
        for i in range(left, right):
            working[i] = nums[i]  # use working[left:right] as working memory

        li, ri = left, mid
        for i in range(left, right):
            if ri == right or ((li != mid) and working[li] < working[ri]):
                nums[i] = working[li]
                li += 1
            else:
                nums[i] = working[ri]
                ri += 1

    def sort(left, right):
        if right - left <= 1:
            return
        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, right, mid)

    sort(0, len(nums))


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3, 7]
    print(mergesort(arr))
    assert mergesort(arr) == [1, 2, 3, 4, 5, 6, 7]
    # more mergesort tests with longer arrays
    assert mergesort([3, 4, 6, 5, 2, 1, 9, 8, 7, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("ok")
