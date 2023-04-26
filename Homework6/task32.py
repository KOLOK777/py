# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

def indexes(a, b, c):
    new_list = []
    index_list = []
    for i in range(c):
        new_list.append(random.randint(-10, 11))
        if new_list[i] >= a and new_list[i] <= b:
            index_list.append(i)
    print(f'Сформирован следующий массив: {new_list}')
    print(f'Перечень индексов, удовлетворяющих условию: {index_list}')

while True:
    try:
        min_number = float(input('Введите минимальное значение для проверки: '))
        break
    except ValueError:
        print('Неоходимо ввести число. ')
while True:
    try:
        max_number = float(input('Введите максимальное значение для проверки: '))
        break
    except ValueError:
        print('Неоходимо ввести число. ')
while True:
    try:
        list_number = int(input('Введите количество элементов: '))
        if list_number <= 0:
            raise Exception
        break
    except ValueError:
        print('Неоходимо ввести целое число. ')
    except Exception:
        print('Неоходимо ввести положительное число. ')

indexes(min_number, max_number, list_number)




