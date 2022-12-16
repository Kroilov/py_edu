# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится)

x = int(input('Enter x: '))
y = int(input('Enter y: '))

if x == 0 and y == 0:
    print('Enter valid value')

elif x == 0:
    print('Point on X axis')

elif y == 0:
    print('Point on Y axis')

elif x > 0 and y > 0:
    print('First quarter')

elif x < 0 and y > 0:
    print('Second quarter')

elif x < 0 and y < 0:
    print('Third quarter')

elif x > 0 and y < 0:
    print('Fourth quarter')