my_array = [1, 2, 5, 10, 6, 13, 44, 12, 0, -1, -99]
print("Linear Search for sorted/ unsorted array")


def linearsearch(value, givenlist):
    for i in range(len(givenlist)):
        if givenlist[i] == value:
            return i

    return False


print(linearsearch(-1, my_array))

# Sorted array searching: Binary Search
my_array2 = [-99, -45, -1, 0, 9, 23, 44, 100, 120, 1201]


def binarysearch(value, givenlist):
    first = 0
    last = len(givenlist) - 1

    while first <= last:
        mid = (first + last) // 2
        if givenlist[mid] == value:
            return mid
        elif givenlist[mid] > value:
            last = mid - 1
        else:
            first = mid + 1

    return False


print(binarysearch(-99, my_array2))
