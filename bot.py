from telegram import update
from telegram.ext import Upadater, commandhandler, updater
import telebot
import logging
from telebot import types
from telebot.apihelper import ApiTelegramException
from time import time



def start(uodate, context):

    updater.message.replay_text('hello, humano')

if __name__ == '__main__':

    updater = Upadater(token='5056427888:AAFKgOpSXU8Fw3DgiMUQgV81CHtMdsPtiDE', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(commandhandler('start', start))

    updater.start_polling()
    updater.idle()

    