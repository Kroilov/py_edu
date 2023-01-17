import telebot
import datetime
import numexpr


def start(message):
    bot.send_message(message.chat.id, 'Я калькубот! Что нужно посчитать?')


def handle_text(message):
    bot.send_message(message.chat.id, parse(message.text, message.chat.id))


def log(message, chat_id):
    with open("log.txt", "a") as logfile:
        logfile.write(str(datetime.datetime.now()) + "\t" +
                      str(chat_id) + "\t" + message + "\n")


def calc(arg_str):
    return str(numexpr.evaluate(arg_str))


def parse(text, chat_id):
    try:
        if text == "/help":
            result = "Пишите пример в чат без всяких комманд. \n*В калькуляторе использована библиотека numexpr"
            log(text, chat_id)
        else:
            result = calc(text)
            log(text, chat_id)
    except:
        result = "Ошибка! Повторите ввод."
        log("Error: \t" + text, chat_id)
    return result


bot = telebot.TeleBot(token="TOKEN")
bot.message_handler(commands=["start"])(start)
bot.message_handler(content_types=["text"])(handle_text)
bot.polling(none_stop=True, interval=0)
