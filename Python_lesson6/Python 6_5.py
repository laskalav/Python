class Stationery (object):
    def __init__(self, tittle):
        self.tittle = tittle

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Начинаем рисовать ручкой")


class Pencil (Stationery):
    def draw(self):
        print("Запускаем отрисовку карандашом")


class Handle (Stationery):
    def draw(self):
        print("Начинаем рисовать маркером")



if __name__ == '__main__':
    pen = Pen(tittle="Ручка")
    pen.draw()
    pencil = Pencil(tittle="Карандаш")
    pencil.draw()
    handle = Handle(tittle="Маркер")
    handle.draw()