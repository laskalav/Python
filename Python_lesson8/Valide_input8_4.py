from Python_lesson8.Python8_4 import Warehouse, Printer, Scanner, Xerox
warehouse1 = Warehouse()
warehouse2 = Warehouse()

while True:
    choice = input("Какой товар добавить на склад?\n 1 - Принтер \n 2 - Сканер \n 3 - Ксерокс\n")
    if choice == "1":
        choice_equip = Printer(weight=100,
                               name = "HP",
                               color="white",
                               print_type="laser")
    elif choice == "2":
        choice_equip = Scanner(weight=100,
                               name="HP",
                               color="white",
                               resolution="A4")
    elif choice == "3":
        choice_equip = Xerox(weight=100,
                             name="HP",
                             color="white",
                             speed=500)
    else:
        print("Некорректный выбор")
        break

    num_choice = input("Сколько единиц товара добавить?\n")
    if num_choice.isdigit():
        num_choice = int(num_choice)
    else:
        print("Вы ввели не число!")
        break

    for i in range(num_choice):
        warehouse1.storage_office_equipment(choice_equip)

print(warehouse1.storage)





