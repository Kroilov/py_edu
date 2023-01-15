import telebot
import numpy as np
import random


def init_board():
    global board, player
    board = np.array([[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']])
    player = 'X'


def start_game(message):
    init_board()
    bot.send_message(
        message.chat.id,
        f"Welcome to Tic-Tac-Toe!\nUse the commands row col to make your move.\n<code>{print_board(board)}</code>\nPlayer X starts.",
        parse_mode='HTML')


def play(message):
    global board, player
    try:
        row, col = [int(x) for x in message.text.split()]
        row, col = row - 1, col - 1
        if board[row][col] == ' ':
            board[row][col] = player
            bot.send_message(
                message.chat.id, f"{player}'s turn\n<code>{print_board(board)}</code>", parse_mode='HTML')
            player = 'O'
        else:
            bot.send_message(
                message.chat.id, "That spot is already taken, try again.")
    except:
        bot.send_message(
            message.chat.id, "Invalid command, please use row col (e.g 1 1).")
    check_winner(board, message)
    if player == "O":
        empty_cells = np.where(board == ' ')
        index = random.randint(0, len(empty_cells[0]) - 1)
        row, col = empty_cells[0][index], empty_cells[1][index]
        board[row][col] = player
        player = 'X'
        bot.send_message(message.chat.id, f'Bot moves to {row + 1}, {col + 1}\n<code>{print_board(board)}</code>', parse_mode='HTML')
        check_winner(board, message)

def print_board(board):
    printed_board = ''
    for row in board:
        printed_board = printed_board + '|'.join(row) + '\n'
    return printed_board


def check_board(board):
    for row in range(board.shape[0]):
        if len(set(board[row])) == 1 and board[row][0] != ' ':
            return board[row][0]
    for col in range(board.shape[1]):
        if len(set(board[:, col])) == 1 and board[0][col] != ' ':
            return board[0][col]
    if len(set(board.diagonal())) == 1 and board[0, 0] != ' ':
        return board[0, 0]
    if len(set(np.fliplr(board).diagonal())) == 1 and board[0, -1] != ' ':
        return board[0, -1]


def check_winner(board, message):
    winner = check_board(board)
    if winner:
        print_board(board)
        bot.send_message(
            message.chat.id, f'{winner} wins!\nNew game started.')
        init_board()
    if not np.any(board == ' '):
        print_board(board)
        bot.send_message(
            message.chat.id, 'Tie!\nNew game started.')
        init_board()
    

bot = telebot.TeleBot(token="5815785408:AAENbxtAVAfofJ8VgOXbolqyqKbG_oYnSeg")
bot.message_handler(commands=['start'])(start_game)
bot.message_handler(content_types=["text"])(play)
bot.polling()
