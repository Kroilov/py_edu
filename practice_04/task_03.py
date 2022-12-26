# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

from random import randint

n = int(input('Enter sequence size: '))
list = []
for i in range(n):
    list.append(randint(0, 10))

print(f'Generated sequence: {list}')
print(f'Unic numbers: {set(list)}')
