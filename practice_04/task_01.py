# Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

pi = 1
for i in range(1, 1000000):
    pi += ((-1) ** i) * (1 / (2 * i + 1))
pi *= 4

print(round(pi, int(input('Enter the number of decimal: '))))