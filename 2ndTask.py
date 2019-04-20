#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random


with open('/Users/alina/Downloads/sayings-2.tsv', encoding='utf-8') as f:
    originals = f.read()


codes = ('пов,2-л',
         'нп=непрош,ед,изъяв,3-л',
         'мн,изъяв,1-л',
         'ед,кр,муж',
         'нп=непрош,ед,изъяв,3-л,сов',
         'нп=непрош,ед,изъяв,3-л,несов',
         'прош,мн,изъяв,сов,пе',
         'прош,мн,изъяв,сов,пе',
         'нп=прош,ед,изъяв,сред,сов',
         '=V,пе=инф,несов')


def generator(first_halves, second_halves):
    possible_first = []
    possible_second = []
    code = random.choice(codes)
    if code != '—':
        for i, half in enumerate(second_halves):
            if code in half:
                possible_second.append(half)
                first_halves[i] = first_halves[i] + '{' + code + '}'
                possible_first.append(first_halves[i])
        for half in first_halves:
            if code in half:
                possible_first.append(half)
    else:
        for i, half in enumerate(first_halves):
            if code in half:
                possible_first.append(half)
                second_halves[i] = second_halves[i] + '{' + code + '}'
                possible_second.append(second_halves[i])
    saying = random.choice(possible_first) + ' ' + random.choice(possible_second)
    return saying


def clean_output(saying):
    saying = re.sub('{.+?}', '', saying)
    return saying


def func():
    with open('/Users/alina/Downloads/first_halves.txt', encoding='utf-8') as f:
        first_halves = f.read().split('\n')
    with open('/Users/alina/Downloads/second_halves.txt', encoding='utf-8') as f:
        second_halves = f.read()
        second_halves = second_halves.split('\n')
    saying = 'Яблоко от яблони недалеко падает'
    while saying in originals:
        saying = clean_output(generator(first_halves, second_halves))
    return saying + '.'



"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
import time
from telegram.error import NetworkError, Unauthorized
from telegram.ext import Updater
from telegram.ext import Dispatcher
from telegram.ext import CommandHandler

working = False

update_id = None
all_users = set()
bot = telegram.Bot('665264585:AAGKtB2h8jIdiMhFYvtzUH4mjHAbBKZUUFM')

count = 0

users_time = {}

def start(id, chatFile):
    global bot, all_users, working
    bot.send_message(chat_id=id, text="Вы будете получать смешные поговорки каждую минуту!")
    print(id)
    working = True
    users_time[id] = time.time()
    if (str(id) not in all_users):
        all_users.add(str(id))
        chatFile.write(str(id) + "\n")


msg = func()

def main():
    global msg, count
    """Run the bot."""
    global update_id
    global all_users
    global bot
    with open("chats", "r") as chatFile:
        for line in chatFile:
            all_users.add(str(line).strip())
    print("File loaded!")
    # Telegram Bot Authorization Token
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
    print("Starting bot!")
    while True:
        sendAll()
        echo(bot)


def echo(bot):
    global update_id
    global all_users
    global users_time
    # Request updates after the last update_id
    with open("chats", "a") as chatFile:
        for update in bot.get_updates(offset=update_id):
            update_id = update.update_id + 1
            if update.message:  # your bot can receive updates without messages
                msgText = update.message.text
                if (msgText == "/start"):
                    start(update.message.chat.id, chatFile)
                else:
                    try:
                        print(1)
                    except:
                        bot.send_message(chat_id=update.message.chat.id, text="Лучше ничего не пишите : )")
                # update.message.reply_text(update.message.text)

def sendAll():
    global msg
    print("HERE")
    global all_users, users_time
    global bot
    for line in all_users:
        id = int(line.strip())
        if (time.time() - users_time[id] >= 45):
            users_time[id] = time.time()
            bot.send_message(chat_id=id, text=msg)
            msg = func()


if __name__ == '__main__':
    main()
