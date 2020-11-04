class DivZero(Exception):
    pass


num1 = input("Введите число:")
num2 = input("Введите число:")
try:
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        raise DivZero()
    sum = num1 / num2
except ValueError:
    print("Вы ввели не число!")
except DivZero:
    print("Вы ввели 0!")
else:
    print(sum)




