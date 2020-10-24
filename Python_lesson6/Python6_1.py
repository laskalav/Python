from time import sleep


class TrafficLight(object):
    def __init__(self):
        self._colors = ["Красный", "Желтый", "Зеленый"]
        self.delays = [7, 2, 10]
        self.color = None

    def running(self):
        self.color = self._colors[0]

        while True:
            print(self.color)
            sleep(self.delays[self._colors.index(self.color)])
            self.switch()

    def switch(self):
        state = self._colors.index(self.color)
        if state + 1 >= len(self._colors):
            self.color = self._colors[0]
        else:
            self.color = self._colors[state + 1]


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()
