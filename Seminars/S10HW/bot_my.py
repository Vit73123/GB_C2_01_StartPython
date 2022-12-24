from telegram.ext import\
        ApplicationBuilder,\
        CommandHandler,\
        MessageHandler,\
        filters
from commands import *

dispatcher = ApplicationBuilder().token("TOKEN").build()

start_handler = dispatcher.add_handler(CommandHandler('start', start))
expr_handler = dispatcher.add_handler(CommandHandler('calc', expr))
calc_handler = dispatcher.add_handler(MessageHandler(filters.TEXT, calc))

print('server start')
dispatcher.run_polling()