import telegram

# Connect to our bot
bot = telegram.Bot(token="256474863:AAHCu547v1mc2SBMT2DpbM8fN6wLEPFUih8")
while True:
    # Waits for the first incoming message
    updates=[]
    txt = "I do not understand! Explain! *Explain!*"
    while not updates:
        updates = bot.getUpdates()

    print(updates[-1].message.text)
    chat_id=updates[-1].message.chat_id
    if updates[-1].message.text == "Exterminate!":
        break
    elif ("dr" in updates[-1].message.text) or ("doctor" in updates[-1].message.text):
        txt = "You are... the Doctor! You must be exterminated!"
    bot.sendMessage(chat_id=chat_id, text="%s"%txt,parse_mode=telegram.ParseMode.MARKDOWN)
