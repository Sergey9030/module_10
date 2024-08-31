from threading import Thread  # Работа с потоками
from datetime import datetime
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
print('Время работы функций:', time_end - time_start, 'сек.')

time_start = datetime.now()

thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))  # Создали поток
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))  # Создали поток
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))  # Создали поток
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))  # Создали поток

thr_1.start()  # Запускаем поток
thr_2.start()  # Запускаем поток
thr_3.start()  # Запускаем поток
thr_4.start()  # Запускаем поток

thr_1.join()  # Ждем завершения работы потока
thr_2.join()  # Ждем завершения работы потока
thr_3.join()  # Ждем завершения работы потока
thr_4.join()  # Ждем завершения работы потока

time_end = datetime.now()
print('Время работы потоков:', time_end - time_start, 'сек.')
