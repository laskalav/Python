from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def expenditure(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def expenditure(self):
        return 2 * self.size + 0.3


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    def expenditure(self):
        return self.height / 6.5 + 0.5


if __name__ == '__main__':
    coat = Coat(size=42)
    costume = Costume(height=170)
    amount = coat.expenditure() + costume.expenditure()
    amount = round(amount, 2)
    print(f"Всего ткани потрачено: {amount}")


