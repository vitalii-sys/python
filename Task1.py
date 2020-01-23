from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        a = [0, 1, 2]
        for i in cycle(a):
            print(f'Switching color to\n'
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(4)


TrafficLight = TrafficLight()
TrafficLight.running()
