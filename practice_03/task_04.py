# Напишите программу, которая будет преобразовывать десятичное число в двоичное


def convert_to_bin(in_num):
    if in_num != 1:
        convert_to_bin(in_num // 2)
    print(in_num % 2, end='')

in_num = int(input('Enter number: '))
convert_to_bin(in_num)