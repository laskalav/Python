class OfficeEquipment(object):
    def __init__(self, weight, name, color):
        self.weight = weight
        self.name = name
        self.color = color
        self.class_name = None


class Warehouse(object):
    def __init__(self):
        self.storage = {}

    def storage_office_equipment(self, equipment: OfficeEquipment):
        if not self.storage.get(equipment.class_name):
            self.storage[equipment.class_name] = [equipment]
        else:
            self.storage[equipment.class_name].append(equipment)

    def remove_equipment(self, equipment: OfficeEquipment):
        if equipment in self.storage.get(equipment.class_name, []):
            shelf = self.storage[equipment.class_name]  # type: list
            equip_index = shelf.index(equipment)
            res_equipment = shelf.pop(equip_index)
            return res_equipment
        else:
            print("Такого оборудования нет на складе")

    def transfer_equipment(self, equipment: OfficeEquipment, other_warehouse):
        trans_equip = self.remove_equipment(equipment)
        if trans_equip:
            other_warehouse.storage_office_equipment(trans_equip)


class Printer(OfficeEquipment):
    def __init__(self, weight, name, color, print_type):
        super().__init__(weight, name, color)
        self.print_type = print_type
        self.class_name = 'Printer'


class Scanner(OfficeEquipment):
    def __init__(self, weight, name, color, resolution):
        super().__init__(weight, name, color)
        self.resolution = resolution
        self.class_name = 'Scanner'


class Xerox(OfficeEquipment):
    def __init__(self, weight, name, color, speed):
        super().__init__(weight, name, color)
        self.speed = speed
        self.class_name = 'Xerox'


if __name__ == '__main__':
    printer = Printer(weight=100,
                      name="HP",
                      color="red",
                      print_type="laser")
    warehouse = Warehouse()
    warehouse.storage_office_equipment(printer)