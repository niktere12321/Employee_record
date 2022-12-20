import datetime
import os
import sqlite3
from random import randint

import telebot
import xlsxwriter
from db import Users, engine
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from telebot import types

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main_menu(message):
    keyboard = types.ReplyKeyboardMarkup(
        row_width=1,
        resize_keyboard=False,
        one_time_keyboard=True
    )
    button = types.KeyboardButton(text='Записать работника')
    keyboard.add(button)
    bot.send_message(
        message.chat.id,
        'Вы в главном меню',
        reply_markup=keyboard
    )
    bot.register_next_step_handler(message, button_message)


def button_message(message):
    if message.text == "Записать работника":
        bot.send_message(
            message.chat.id,
            "Введите ФИО работника",
            reply_markup=types.ReplyKeyboardRemove()
        )
        bot.register_next_step_handler(message, get_data)
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')
        main_menu(message)


def get_data(message):
    if len(message.text.split(' ')) == 3:
        new_user = Users(
            fio=message.text,
            datar=datetime.date(randint(1980, 2005), randint(1, 12), randint(1, 28)),
            id_role=randint(1, 2)
        )
        session.add(new_user)
        session.commit()
        con = sqlite3.connect('../sqlite.db')
        cur = con.cursor()
        cur.execute('''
        SELECT fio,
               datar,
               (SELECT name FROM roles WHERE id = users.id_role)
        FROM users
        ORDER BY id DESC
        LIMIT 5;
        ''')
        workbook = xlsxwriter.Workbook('data.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'ФИО')
        worksheet.write('B1', 'Дата рождения')
        worksheet.write('C1', 'Наименование роли')
        row = 1
        col = 0
        for item in cur:
            for i in range(3):
                worksheet.write(row, col + i, item[i])
            row += 1
        workbook.close()
        con.close()
        with open('data.xlsx', 'rb') as workbook:
            bot.send_document(message.chat.id, workbook)
        main_menu(message)
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')
        main_menu(message)


if __name__ == '__main__':
    session = Session(engine)
    bot.polling(none_stop=True)
