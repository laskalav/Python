class Road(object):
    def __init__(self, lenght, width,asphalt):
        self.__lenght = lenght
        self.__width = width
        self.__asphalt = asphalt

    def building_road(self):
        res = self.__lenght * self.__width * self.__asphalt.massa * self.__asphalt.height
        print(res)
        return res


class Asphalt(object):
    def __init__(self, massa, height):
        self.massa = massa
        self.height = height


if __name__ == '__main__':
    asphalt = Asphalt(massa=25,
                      height=5)
    road = Road(lenght=5000,
                width=20,
                asphalt=asphalt)
    print(road.building_road())