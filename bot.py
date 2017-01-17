import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, ConversationHandler, RegexHandler
from telegram.replykeyboardmarkup import *
updater = Updater(token="256474863:AAHCu547v1mc2SBMT2DpbM8fN6wLEPFUih8")
dispatcher = updater.dispatcher

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)
identity_keyboard = [['Human', 'Dalek'],
                  ['Cyberman', 'Weeping Angel'],]
markup_id = ReplyKeyboardMarkup(identity_keyboard, one_time_keyboard=True)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    update.message.reply_text(chat_id=update.message.chat_id, text="We are the Daaaalek! *Identify! Identify!*",parse_mode=telegram.ParseMode.MARKDOWN,reply_markup=markup_id)
    return CHOOSING

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def regular_choice(bot, update, user_data):
    text = update.message.text
    if text != "Dalek":
        voice = open('sounds/Exterminate.mp3', 'rb')
        bot.sendVoice(update.message.chat_id,voice)

def custom_choice(bot, update, user_data):
    pass

def done(bot,update):
    pass
#handling start command
conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CHOOSING: [RegexHandler('^(Human|Dalek|Cyberman|Weeping Angel)$',
                                    regular_choice,
                                    pass_user_data=True),
                       RegexHandler('^Something else...$',
                                    custom_choice),
                       ],
        },

        fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
    )

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()

# while True:
#     # Waits for the first incoming message
#     updates=[]
#     txt = "I do not understand! Explain! *Explain!*"
#     while not updates:
#         updates = bot.getUpdates()
#
#     print(updates[-1].message.text)
#     chat_id=updates[-1].message.chat_id
#     if updates[-1].message.text == "Exterminate!":
#         break
#     elif ("dr" in updates[-1].message.text) or ("doctor" in updates[-1].message.text):
#         txt = "You are... the Doctor! You must be exterminated!"
#     bot.sendMessage(chat_id=chat_id, text="%s"%txt,parse_mode=telegram.ParseMode.MARKDOWN)
