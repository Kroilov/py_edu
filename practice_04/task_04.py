# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

k = int(input('Enter K: '))
for i in range(k, 0, -1):
    x = randint(0, 100)
    if i == k:
        print(f'{x}x^{i}', end=' ')
    elif i == 1:
        print(f'+ {x}x', end=' ')
    else:
        print(f'+ {x}x^{i}', end=' ')

print(f'+ {randint(0, 100)} = 0')