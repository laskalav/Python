class NumList(Exception):
    pass


num_list = []
while True:
    try:
        num = input("Введите число:")
        if num == "stop":
            print(num_list)
            break
        if not num.isdigit():
            raise NumList()
        num_list.append(num)
    except NumList:
        print("Введено не число!")





