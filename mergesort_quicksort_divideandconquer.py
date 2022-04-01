# write a prog to sort the nos.

a = [4, 2, 6, 3, 4, 6, 2, 1]
b = [4, 1, 2]


def sort(nums):
    pass


# bubble sort

def bubble_sort(nums):
    nums = list(nums)
    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    print(nums)


bubble_sort(a)

"""
Complexity of bubble_sort: Time complexity:  (n-1)*(n-1)= n^2  O(n^2)
Space complexity is O(n)
"""


# insertion Sort

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j + 1, cur)
    print(nums)


insertion_sort(a)

"""
Complexity of insertion_sort: Time complexity:  (n)*(n-1)= n^2 : O(n^2)
Space complexity is O(n)
"""


def merge(num1, num2):
    i, j = 0, 0
    merged = []

    while i < len(num1) and j < len(num2):
        if num1[i] <= num2[j]:
            merged.append(num1[i])
            i += 1
        else:
            merged.append((num2[j]))
            j += 1

    rest_num1 = num1[i:]
    rest_num2 = num2[j:]

    return merged + rest_num1 + rest_num2


# divide and conqure  - (Merge Sort)
def merge_sort(nums):
    num_len = len(nums)
    if num_len <= 1:
        return nums

    mid = num_len // 2
    left = nums[:mid]
    right = nums[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    sorted_nums = merge(left_sorted, right_sorted)
    return sorted_nums


print(merge_sort(a))


"""
Complexity of insertion_sort: Time complexity:  O(nlogn)
Space complexity is O(nlogn)
Additional space complexity O(n)
"""


# ToDo: Quick sort algorithm

def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot - 1)
        quick_sort(nums, pivot + 1, end)

    return nums


def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1

    l, r = start, end - 1

    while l < r:
        if nums[l] <= nums[end]:
            l += 1

        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]

    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l

    else:
        return end


print(quick_sort(a))

"""
Complexity of insertion_sort: Time complexity: avg:  O(nlogn), worst case: O(n^2)
Space complexity is O(n)
Additional space complexity O(1)
"""

