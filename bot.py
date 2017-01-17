import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, ConversationHandler, RegexHandler
from telegram.replykeyboardmarkup import *

tokenfile = open("bot_token","r")
token = tokenfile.readline().strip()
updater = Updater(token=token)
dispatcher = updater.dispatcher

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)
identity_keyboard = [['Human', 'Dalek'],
                  ['Cyberman', 'Weeping Angel'],
                  ['Rose Tyler'],]
markup_id = ReplyKeyboardMarkup(identity_keyboard, one_time_keyboard=True)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    update.message.reply_text("We are the Daaaalek! *Identify! Identify!*", parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=markup_id)
    return CHOOSING

def echo(bot, update):
    bot.sendMessage(update.message.text)

def regular_choice(bot, update, user_data):
    text = update.message.text
    if "Rose Tyler" in text:
        bot.sendMessage(update.message.chat_id, "* Genetic material extrapolated! Initiating reconstruction! *", parse_mode=telegram.ParseMode.MARKDOWN)
    elif text != "Dalek":
        voice = open('sounds/Exterminate.mp3', 'rb')
        bot.sendVoice(update.message.chat_id, voice)
    else:
        voice = open('sounds/Go_stronger.mp3', 'rb')
        bot.sendVoice(update.message.chat_id, voice)

def custom_choice(bot, update, user_data):
    text = update.message.text
    logging.info(text)
    if ("dr" in text.lower()) or ("doctor" in text.lower()):
        voice = open('sounds/Exterminate.mp3', 'rb')
        bot.sendVoice(update.message.chat_id, voice)
        bot.sendMessage(update.message.chat_id, "We are the Daaaalek! \n You are the doctor \n *The doctor must die!* \n *Exterminaaaaate!!! Exterminate!!!*", parse_mode=telegram.ParseMode.MARKDOWN)

    else:
        bot.sendMessage(update.message.chat_id,
                        "We are the Daaaalek! \n You are " + text + " \n *Exterminate!!! Exterminate!!!*",
                        parse_mode=telegram.ParseMode.MARKDOWN)
        voice = open('sounds/Exterminate.mp3', 'rb')
        bot.sendVoice(update.message.chat_id, voice)

def done(bot,update):
    bot.sendMessage(update.message.chat_id, "Stay!", parse_mode=telegram.ParseMode.MARKDOWN)
    voice = open('sounds/Stay.mp3', 'rb')
    bot.sendVoice(update.message.chat_id, voice)

    return ConversationHandler.END



#handling start command
conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CHOOSING: [RegexHandler('^(Human|Dalek|Cyberman|Weeping Angel|Rose Tyler)$',
                                    regular_choice,
                                    pass_user_data=True),
                       RegexHandler('^(Bye|Done|Cu|Got to go|So long|I am too old for this shit|goodbye)$',
                                    done),
                       MessageHandler(Filters.text,
                                    custom_choice, pass_user_data=True),
                       ],
        },

        fallbacks=[RegexHandler('^Done$', done)]
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
