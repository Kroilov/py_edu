# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

new_list = [3, 4, 5, 6, 7, 8, 9]
final_list = []
for i in range((len(new_list) + 1) // 2):
        final_list.append(new_list[i] * new_list[len(new_list) - i -1])

print(final_list)




# var 2
#
# if len(new_list) % 2 == 0:
#     len_list = len(new_list) // 2
# else:
#     len_list = len(new_list) // 2 + 1
# for i in range(len_list):
#     print(new_list[i] * new_list[len(new_list) - i -1])