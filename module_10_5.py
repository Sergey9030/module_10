import multiprocessing
import os
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        s = file.readline()
        while len(s) > 0:
            all_data.append(s)
            s = file.readline()


if __name__ == '__main__':

    directory = "./Files"
    files = os.listdir(directory)  # Читаем список файлов
    files = [directory + '/' + f for f in files]  #Добавляем к имени файла путь

    # Линейный вызов
    start = datetime.now()
    for f in files:
        read_info(f)
    print(f'{datetime.now()-start} (линейный)')

    # Многопрцессорный вызов
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    print(f'{datetime.now()-start} (многопроцессорный)')
