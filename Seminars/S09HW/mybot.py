from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import *

app.add_handler(CommandHandler("filter", filter_command))

print('server start')
app.run_polling()