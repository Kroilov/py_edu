# Создайте программу для игры в ""Крестики-нолики""

board = [[" " for i in range(3)] for j in range(3)]


def print_board():
    print('-------')
    for row in board:
        print('', end=' ')
        for cell in row:
            print(cell, end=" ")
        print()
    print('-------')


def make_move(x, y, player):
    if board[x][y] != ' ':
        print('Choose another cell, this one is occupied!')
        return
    board[x][y] = player


def check_win(player):
    for row in board:
        if row == [player, player, player]:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_draw():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


while True:
    print_board()
    x, y = map(int, input('Enter coord. for X: ').split())
    x, y = x - 1, y - 1
    if x < 0 or x > 2 or y < 0 or y > 2:
        print("Enter space-separated coordinates from 1 to 3 for x and y!")
        continue
    make_move(x, y, "X")
    if check_win('X'):
        print_board()
        print('X wins!')
        break
    if check_draw():
        print_board()
        print('Draw.')
        break

    print_board()
    x, y = map(int, input('Enter coord. for O: ').split())
    x, y = x - 1, y - 1
    if x < 0 or x > 2 or y < 0 or y > 2:
        print("Coordinates should be from 1 to 3 for x and y!")
        continue
    make_move(x, y, "O")
    if check_win('O'):
        print_board()
        print('O wins!')
        break
    if check_draw():
        print_board()
        print('Draw.')
        break
