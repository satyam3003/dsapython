# Merge Sort
unsorted_array = [1, -100, 125, 44, 33, 22, -1000, 2]


def mergesort(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    else:
        mid = arr_len // 2
        left_sort = mergesort(arr[:mid])
        right_sort = mergesort(arr[mid:])

        sorted_arr = merge(left_sort, right_sort)
        return sorted_arr


def merge(left_a, right_a):
    l, r = 0, 0
    merged_arr = []
    while l <= len(left_a) - 1 and r <= len(right_a) - 1:
        if left_a[l] <= right_a[r]:
            merged_arr.append(left_a[l])
            l += 1
        else:
            merged_arr.append(right_a[r])
            r += 1

    return merged_arr + left_a[l:] + right_a[r:]


print("Merge Sort nlog(n)")
print(f"unsorted_array: {unsorted_array}")
print(f"sorted_array: {mergesort(unsorted_array)}")


def quicksort(arr):
    pass
