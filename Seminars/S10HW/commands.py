from telegram import Update
from telegram.ext import ContextTypes
import digit, log                       # , in_num

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):   
    await update.message.reply_text('/calc')

async def expr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Введите выражение')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    primer = digit.parse(update.message.text)
    result = digit.calculate(primer)
    result = "".join(map(str, primer)) + ' = ' + str(result)
    log.loger(
        primer,
        result,
        update.effective_user.id,
        update.effective_user.first_name)
    await update.message.reply_text(result)
    await update.message.reply_text('Хотите продолжить? Наберите команду\n/calc')