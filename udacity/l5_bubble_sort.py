my_array = [1, 4, 2, 6, 4, 10, 12, 3, 20, 18]

for i in range(len(my_array)):
    for j in range(i):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print(my_array)
