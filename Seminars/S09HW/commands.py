from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def msg_filter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text(' '.join([word for word in update.message.text.split() if not 'абв' in word]))