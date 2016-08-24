# def fibonacci(a, b):
#     c = a + b
#     sum = 2;
#     while (c <= 4000000):
#         if (c % 2 == 0):
#             sum = sum + c
#         a, b = b, c
#         c = a + b
#     print(a)
#     print(b)
#     print(c)
#     print(sum)
#
#
# fibonacci(a=1, b=2)


def fibonacci(maxi):
    a, b = 0, 1
    while a < maxi:
        yield a
        print("calculating a")
        a, b = b, a + b

# fib_list = fibonacci(100)
# for i in fib_list:
#     print(i)
# for i in fib_list:
#     print(i)

fib_list= fibonacci(1000)
print(fib_list)
print(next(fib_list))
print(next(fib_list))
print(next(fib_list))
print(next(fib_list))
print(next(fib_list))
print(next(fib_list))


