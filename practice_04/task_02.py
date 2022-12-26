# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

import math

number = int(input("Enter number: "))

for i in range(2, int(math.sqrt(number)) + 1):
    while (number % i == 0):
        print(i)
        number //= i

if (number != 1):
    print(number)
