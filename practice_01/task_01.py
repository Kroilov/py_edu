# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным

n = int(input('Enter day: '))
if 6 > n > 0:
    print('Weekday')
elif n == 6 or n == 7:
    print('Weekend')
else:
    print('Enter day number from 1 to 7')
