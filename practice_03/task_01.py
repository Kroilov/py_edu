# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

new_list = [3, 5, -5, 10, 6]
sum = 0
for i in range(1, len(new_list), 2):
    sum += new_list[i] 
print(sum)


# var 2:
#
# for i in range(len(new_list)):
#     if i % 2 != 0:
#         sum = sum + new_list[i]
# print(sum)