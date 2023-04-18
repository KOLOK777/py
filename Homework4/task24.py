# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9
number_bushes = int(input('Введите количество кустов: '))
effect_list = []
for i in range(number_bushes):
    effect_list.append(int(input(f'Введите урожайность куста № {i+1}: ')))
max_berries = effect_list[0] + effect_list[1] + effect_list[number_bushes - 1]
bush_number = 1
for i in  range(1, number_bushes-1):
    if effect_list[i - 1] + effect_list[i] + effect_list[i + 1] > max_berries:
        max_berries = effect_list[i - 1] + effect_list[i] + effect_list[i + 1]
        bush_number = i+1
if effect_list[0] + effect_list[number_bushes - 2] + effect_list[number_bushes-1] > max_berries:
    max_berries = effect_list[0] + effect_list[number_bushes - 2] + effect_list[number_bushes-1]
    bush_number = number_bushes
print(f'С куста № {bush_number} и соседних можно собрать максиммальное количество ягод: {max_berries}')

