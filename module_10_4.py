from threading import Thread  # Потоки
import queue  # Очередь
from time import sleep  # Дата-время
from random import randint
from datetime import datetime


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))
        print(f'{datetime.now()}: {self.name} зовет официанта')


class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        i = 0
        for t in self.tables:
            # Рассаживаем гостей за столики
            if i in range(len(guests)):
                t.guest = guests[i]
                t.guest.start()
                print(f'{datetime.now()}: {t.guest.name} сел(-а) за стол номер {t.number}')
                i += 1
        while i in range(len(guests)):
            # Оставшихся гостей ставим в очередь
            self.queue.put(guests[i])
            print(f'{datetime.now()}: {guests[i].name} в очереди')
            i += 1

    def discuss_guests(self):
        while (not self.queue.empty()) or (not self.tables_is_emty()):
            for t in self.tables:
                if (not (t.guest is None)) and (not t.guest.is_alive()):
                    print(f'{datetime.now()}: {t.guest.name} покушал(-а) и ушёл(ушла)')
                    t.guest = None
                    print(f'{datetime.now()}: Стол номер {t.number} свободен')
                    if not self.queue.empty():
                        t.guest = self.queue.get()
                        print(f'{datetime.now()}: {t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}')
                        t.guest.start()
                    else:
                        print(f'{datetime.now()}: Очередь пуста')

    def tables_is_emty(self):  # Определяет, что все столы пусты
        for t in self.tables:
            if not (t.guest is None):
                return False
        return True

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
print(f'{datetime.now()}: Кафе открылось')
# Приём гостей
cafe.guest_arrival(*guests)
print(f'{datetime.now()}: Гости приняты')
# Обслуживание гостей
cafe.discuss_guests()
print(f'{datetime.now()}: Кафе закрылось')
