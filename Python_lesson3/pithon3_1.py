def my_func(a, b):
    return a / b


first_digit = int(input("введите первое число:"))
second_digit = int(input("введите второе число:"))
if second_digit is 0:
    print("Делить на ноль нельзя! Ай ай ай!")
else:
    print(my_func(first_digit, second_digit))
