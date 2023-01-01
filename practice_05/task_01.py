# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты
# оппонента достаются сделавшему последний ход. Сколько конфет
# нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


total = 110
max_take = 30
count = 0  # определяем, чей ход

while total > 0:
    if count == 0:
        if total > 1:
            if total <= max_take:
                max_take = total
            taken = int(input(f'{total} remains. Take from 1 to {max_take}: '))
            if 0 < taken <= max_take:
                total -= taken          
                if total < 2:
                    print('You won!')
                else:
                    count = 1
            else:
                print('Enter valid number.')
        else:
            total = 0
            print('You won!')

    if count == 1:
        if total <= max_take:
            taken = total
            total -= taken
            print(f'Bot takes {taken}. Bot won!')
        if total > 1:

            # Бот должен каждый раз брать такое количество конфет,
            # чтобы в ящике всё время оставалось нечётное число конфет:
            taken = total - (((total // max_take) * max_take) + 1)
            if taken == -1:
                taken = max_take - 1
            if taken == 0:
                taken = max_take
            print(f'Bot takes {taken}')
            total -= taken
            if total == 0:
                print('Bot won!')
            else:
                count = 0
