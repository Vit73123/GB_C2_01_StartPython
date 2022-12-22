from telegram import Bot, Update
from telegram.ext import    Updater,\
                            CommandHandler,\
                            MessageHandler,\
                            filters,\
                            ConversationHandler,\
                            ApplicationBuilder    #, ContextTypes
from random import randint as rnd

# bot = Bot(token = '5937698617:AAFTiaXrR1aRaXxv-hfusisigtDZE45hIaA')
# updater = Updater(token = '5937698617:AAFTiaXrR1aRaXxv-hfusisigtDZE45hIaA')
# dispatcher = updater.dispatcher
dispatcher = ApplicationBuilder().token("TOKEN").build()

# Бот Диалог
# ----------

A = 0
B = 1

# def start(update, context):
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# def start(update, context):
async def cmd_start(update, context):

    # context.bot.send_message(update.effective_chat.id, 'Hello')
    # update.message.reply_text(update.effective_user.id)
    name = update.effective_user.first_name
    await update.message.reply_text('Привет ' + name + ' как у тебя дела?')
    return A

async def msg_txt_howareyou(update, context):
    msg = update.message.text
    name = update.effective_user.first_name
    if 'хор' in msg.lower():
        await update.message.reply_text('Я рад, что у тебя всё хорошо ' + name)
    else:
        await update.message.reply_text('Не грусти ' + name + ' всё будет хорошо')
    await update.message.reply_text('Как погода ' + name + '?')
    return B

async def msg_txt_weather(update, context):
    msg = update.message.text
    await update.message.reply_text('И у меня такая же погода')
    return ConversationHandler.END

async def cmd_rand(update, context):
    await update.message.reply_text(f'{rnd(1, 100)}')

async def msg_cmd(update, context):
    await update.message.reply_text('Я не знаю таких команд')

async def msg_txt(update, context):
    msg = update.message.text
    name = update.effective_user.first_name
    if 'привет' in msg:
        await update.message.reply_text('И тебе привет ' + name)
    else:
        await update.message.reply_text('Получил текст ' + msg)

async def msg_voice(update, context):
    await update.message.reply_text('Получил голосовое сообщение')

async def msg_voice(update, context):
    await update.message.reply_text('Получил голосовое сообщение')

async def cmd_cancel(update, context):
    name = update.effective_user.first_name
    await update.message.reply_text('До свиданья ' + name)

# start_handler = CommandHandler('start')
# dispatcher.add_handler(start_handler)
cmd_start_handler = dispatcher.add_handler(CommandHandler('start', cmd_start))
# cmd_rand_handler = dispatcher.add_handler(CommandHandler('rand', cmd_rand))
# msg_cmd_handler = dispatcher.add_handler(MessageHandler(filters.COMMAND, msg_cmd))
# msg_voice_handler = dispatcher.add_handler(MessageHandler(filters.VOICE, msg_voice))
msg_txt_howareyou_handler = dispatcher.add_handler(MessageHandler(filters.TEXT, msg_txt_howareyou))
msg_txt_weather_handler = dispatcher.add_handler(MessageHandler(filters.TEXT, msg_txt_weather))
# msg_txt_handler = dispatcher.add_handler(MessageHandler(filters.TEXT, msg_txt))
cmd_cancel_handler = dispatcher.add_handler(CommandHandler('cancel', cmd_cancel))

conv_handler = dispatcher.add_handler(ConversationHandler(entry_points=[cmd_start_handler],
                                                          states={A: [msg_txt_howareyou_handler],
                                                                  B: [msg_txt_weather_handler]},
                                                          fallbacks=[cmd_cancel_handler]))

print('server start')
dispatcher.run_polling()
# updater.idle()