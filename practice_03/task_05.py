# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

n = int(input('Enter range: '))


def fiba(n):
    fiba_list = []
    a = 1
    b = 1
    for i in range(n):
        fiba_list.append(a)
        s = a + b
        a = b
        b = s
        
    a = 0
    b = 1
    for i in range(n + 1):
        fiba_list.insert(0, a)
        s = a - b
        a = b
        b = s
    return fiba_list


print(fiba(n))