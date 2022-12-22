from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def filter_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text.replace('абв', ''))