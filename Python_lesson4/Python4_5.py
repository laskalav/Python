from functools import reduce


def multiply(prev_el, el):
    return prev_el * el


num_list = [n for n in range(100, 1001) if n % 2 == 0]
print(reduce(multiply, num_list))
