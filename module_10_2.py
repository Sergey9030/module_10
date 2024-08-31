from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.warrior_count = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        i = 0
        while self.warrior_count > 0:
            i += 1
            self.warrior_count -= self.power
            print(f'{self.name}, сражается {i} день(дня), осталось {self.warrior_count} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {i} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились')
