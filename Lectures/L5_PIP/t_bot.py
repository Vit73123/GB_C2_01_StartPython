from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import t_bot_commands

app = ApplicationBuilder().token("5937698617:AAFTiaXrR1aRaXxv-hfusisigtDZE45hIaA").build()
app.add_handler(CommandHandler("hi", t_bot_commands.hi_command))
app.add_handler(CommandHandler("time", t_bot_commands.time_command))
app.add_handler(CommandHandler("help", t_bot_commands.help_command))
app.add_handler(CommandHandler("sum", t_bot_commands.sum_command))

print('server start')
app.run_polling()