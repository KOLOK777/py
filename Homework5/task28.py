# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def summa(a, b):
    if a == 0:
        return b
    return summa(a - 1, b + 1)

while True:
    try:
        num1 = int(input('Введите первое число (целое неотрицательное): '))
        if num1 < 0:
            raise  Exception
        break
    except ValueError:
        print('Вы ввели не число/не целое число.')
    except Exception:
        print('Введите неотрицательное число.')
while True:
    try:
        num2 = int(input('Введите второе число (целое неотрицательное): '))
        if num2 < 0:
            raise Exception
        break
    except ValueError:
        print('Вы ввели не число/не целое число.')
    except Exception:
        print('Введите неотрицательное число.')
amount = summa(num1, num2)
print(f'Результат суммы двух чисел {num1} и {num2}: {amount}')