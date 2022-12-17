# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной.

n = int(input('Enter number of coins: '))
sideA = 0
for j in range(n):
    k = int(input(f"Enter side of the coin {sideA + 1}: "))
    if k == 1:
        sideA += 1
if sideA < n / 2:
    print(sideA)
else:
    print(n - sideA)