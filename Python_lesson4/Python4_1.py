from sys import argv


def get_salary(production, rate, bonus):
    """
    Функция вычисления зарплаты
    :param production: Выработка в часах
    :param rate: Ставка в час
    :param bonus: Премия
    :return:
    >>> get_salary(8, 350, 500)
    3300
    """
    return (int(production) * int(rate)) + int(bonus)


if len(argv) == 4:
    print(get_salary(argv[1], argv[2], argv[3]))
else:
    print("Неккоректное количество аргументов для расчета!")
