def my_func(x, y):
    if y >= 0:
        print("Число y не отрицательное!")
        return None
    result = x
    for count in range(1, abs(y)):
        result *= x

    return 1 / result


print(my_func(2, -5), 2 ** -5)
