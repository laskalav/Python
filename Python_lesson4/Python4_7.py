from math import factorial


def fact(n):
    for num in range(1, n):
        yield factorial(num)


print([i for i in fact(10)])
