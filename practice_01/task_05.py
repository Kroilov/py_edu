# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.


import math

aX = float(input('Enter first point X:'))
aY = float(input('Enter first point Y:'))
bX = float(input('Enter second point X:'))
bY = float(input('Enter second point Y:'))

distance = math.sqrt((aX-bX)**2+(aY-bY)**2)
print(f'Distance between points {round(distance, 2)}')