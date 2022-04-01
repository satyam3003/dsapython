def quicksort(arr, start=0, end=None):
    if end is None:
        arr = list(arr)
        end = len(arr) - 1

    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot - 1)
        quicksort(arr, pivot, end)

    return arr


def partition(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    l, r = start, end - 1
    while l < r:
        if arr[l] <= arr[end]:
            l += 1
        elif arr[r] > arr[end]:
            r += 1
        else:
            arr[l], arr[r] = arr[r], arr[l]

    if arr[l] > arr[end]:
        arr[l], arr[end] = arr[end], arr[l]
        return l
    else:
        return end


a = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(a))
