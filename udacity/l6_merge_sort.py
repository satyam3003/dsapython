def merge(num1, num2):
    i, j = 0, 0
    merged = []

    while i < len(num1) and j < len(num2):
        if num1[i] <= num2[j]:
            merged.append(num1[i])
            i += 1
        else:
            merged.append(num2[j])
            j += 1

    remaining_left = num1[i:]
    remaining_right = num2[j:]

    return merged + remaining_left + remaining_right


def merge_sort(num):
    num_len = len(num)
    if num_len <= 1:
        return num

    mid = num_len // 2
    left = num[:mid]
    right = num[mid:]
    left_sort, right_sort = merge_sort(left), merge_sort(right)

    sorted_nums = merge(left_sort, right_sort)
    return sorted_nums


my_array = [1, 4, 2, 6, 4, 10, 12, 3, 20, 18]

print(merge_sort(my_array))
