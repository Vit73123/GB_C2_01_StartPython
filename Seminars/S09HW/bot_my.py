from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from commands import *

dispatcher = ApplicationBuilder().token("TOKEN").build()

dispatcher.add_handler(MessageHandler(filters.TEXT, msg_filter))

print('server start')
dispatcher.run_polling()