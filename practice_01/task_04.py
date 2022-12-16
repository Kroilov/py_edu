# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)


def QuarterSeek():
    
    a = int(input('Enter quarter number (from 1 to 4):'))

    if a == 1:
        print('x > 0, y > 0')
    elif a == 2:
        print('x < 0, y > 0')
    elif a == 3:
        print('x < 0, y < 0')
    elif a == 4:
        print('x > 0, y < 0')
    else:
        QuarterSeek()

QuarterSeek()