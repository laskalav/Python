class Worker(object):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Wage": wage, "Bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["Wage"] + self._income["Bonus"]


if __name__ == '__main__':
    worker = Position(name="Иван",
                      surname="Петров",
                      position="бухгалтер",
                      wage=20000,
                      bonus=5000)

    print(worker.get_full_name())
    print(worker.position)
    print(worker.get_total_income())



