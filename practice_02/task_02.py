# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

n = int(input('Enter N: '))
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)