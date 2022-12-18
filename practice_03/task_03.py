# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

rand_list = []
size = int(input('Enter size of the list: '))

for i in range(size):
    rand_list.append(round(random.uniform(0, 10), 2))
min = rand_list[0] - int(rand_list[i])
max = min
for i in range(len(rand_list)):
    temp_div = rand_list[i] - int(rand_list[i])
    if temp_div > max:
        max = temp_div
    if temp_div < min:
        min = temp_div


print(rand_list)
print(f'Result: {round(max - min, 2)}')