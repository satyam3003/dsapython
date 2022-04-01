unsorted_array = [1, -100, 125, 44, 33, 22, -1000, 2]


# bubblesort n^2
def bubblesort(arr):
    arr = list(arr)
    arr_len = len(arr) - 1
    for i in range(arr_len - 1):
        for j in range(arr_len - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print("\nBubble Sort")
print(f"unsorted_array: {unsorted_array}")
print(f"sorted_array: {bubblesort(unsorted_array)}")


# selection sort n^2
def selectionsort(arr):
    arr = list(arr)
    arr_len = len(arr)
    for i in range(arr_len):
        small_id = i
        for j in range(i + 1, arr_len):
            if arr[j] < arr[small_id]:
                small_id = j

        if i != small_id:
            arr[i], arr[small_id] = arr[small_id], arr[i]

    return arr


print("\nSelection Sort")
print(f"unsorted_array: {unsorted_array}")
print(f"sorted_array: {selectionsort(unsorted_array)}")


# insertion sort n^2
def insertion_sort(arr):
    arr = list(arr)
    len_arr = len(arr)
    for i in range(1, len_arr):
        value = arr[i]
        pos = i
        while pos > 0 and value < arr[pos - 1]:
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos -= 1

    return arr


print("\nInsertion Sort")
print(f"unsorted_array: {unsorted_array}")
print(f"sorted_array: {insertion_sort(unsorted_array)}")
