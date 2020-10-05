proceeds = int(input("Введите количество выручки: "))
costs = int(input("Введите количество издержек: "))
if proceeds > costs:
    profit = proceeds - costs
    print(f"Компания получает прибыль {profit}")
    profitability = profit / proceeds
    print("Рентабельность - %.2f" % profitability)
    staff = int(input("Введите количество сотрудников компании:"))
    profit_staff = profit / staff
    print("Прибыль на одного сотрудника составляет %.2f" % profit_staff)
else:
    print("Коппания работает в убыток")
