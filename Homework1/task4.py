# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

S = int(input('Сколько журавликов сделали Петя, Катя и Сережа ?'))
P = C = S // 6
K = (P + C) * 2
print(f'Петя сделал {P} журавликов, Катя сделала {K} журавликов, а Сережа сделал {C} журавликов.')