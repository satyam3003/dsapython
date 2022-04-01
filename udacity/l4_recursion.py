def fib_se1(num):
    if num < 2:
        return num
    return fib_se1(num-1)+fib_se1(num-2)


print(fib_se1(0))
print(fib_se1(1))
print(fib_se1(2))
print(fib_se1(3))
print(fib_se1(4))
print(fib_se1(5))
print(fib_se1(6))
