def binary_search(my_array, value):
    low = 0
    high = len(my_array) - 1
    while high >= low:
        mid = (high + low) // 2
        if value == my_array[mid]:
            return mid
        elif value > my_array[mid]:
            low = mid + 1
        elif value < my_array[mid]:
            high = mid - 1

    return -1


my_arr = [1, 4, 6, 7, 9, 11, 13, 20]
print(binary_search(my_arr, 13))
print(binary_search(my_arr, 25))
