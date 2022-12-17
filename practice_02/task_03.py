# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n = int(input('Enter N: '))
i = 1
while i <= n:
    i += 1
    if n % i == 0:
        print(i)
        break