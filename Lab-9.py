import random
import logging

# Настройка логгера
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')

file_handler = logging.FileHandler('log.txt')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def main():
    # Ввод количества бочек
    while True:
        try:
            n = int(input('Введите количество бочек: '))
            if n > 0:
                break
            else:
                print('Введено некорректное значение. Попробуйте еще раз.')
        except ValueError:
            print('Введено некорректное значение. Попробуйте еще раз.')

    # Создание списка бочек
    barrels = list(range(1, n+1))

    # Извлечение бочек из мешка
    while barrels:
        input('Нажмите Enter, чтобы вытянуть бочонок: ')
        barrel = random.choice(barrels)
        barrels.remove(barrel)
        print('Вытянут бочонок:', barrel)
        
        # Запись в лог-файл
        logger.info(f'Вытянут бочонок: {barrel}')

    print('Все бочонки извлечены.')



main()