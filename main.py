import telebot
from telebot import TeleBot, types
from functions import encrypter,decrypter

token = 'TOKEN'
link = 'link to your bot'
bot = telebot.TeleBot(token)

#commands

#for command "start"
@bot.message_handler(commands=['start'])
    
def send_welcome(message):
    bot.send_message(message.from_user.id,f'Hello {message.from_user.first_name}👋')
    #buttons
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    markup.row('Message to cipher')
    markup.row('Cipher to message')
    bot.send_message(message.from_user.id,'Choose one:👇',reply_markup=markup)
    

#for command "help"
@bot.message_handler(commands=['help'])
def helping(message):
    textmessage = "After giving /start command, please choose one of 2 buttons. Next send message or cipher.\nWrite with LATIN alphabet letters only.\nDON'T SEND EMOJIS!❌😃"
    bot.reply_to(message,textmessage)
    bot.send_message(message.chat.id,"In order to start please press /start command")

#for command "share"
@bot.message_handler(commands=['share'])
def sharing(message):
    mrkp=types.InlineKeyboardMarkup()
    message_button = types.InlineKeyboardButton(text="Encrypter-decrypter bot",url=link)
    mrkp.add(message_button)
    bot.send_message(message.from_user.id,'Encrypter-decrypter bot is the bot that encryptes and decryptes your messages to make it secure🔓.',reply_markup=mrkp)

#text messages
@bot.message_handler(content_types=['text'])
#for edited messages
@bot.edited_message_handler(content_types=['text'])
def choice(message):
    #cheking message
    if message.text == "Message to cipher":
        bot.reply_to(message,"Please send message...")
        bot.register_next_step_handler(message,convertor1)
    elif message.text=="Cipher to message":
        bot.reply_to(message,'Please send cipher...')
        bot.register_next_step_handler(message,convertor2)

#converting to code
def convertor1(message1):
    bot.reply_to(message1,'Cipher:')
    bot.send_message(message1.chat.id,encrypter(message1.text))

#converting to message
def convertor2(message2):
    bot.reply_to(message2,'Message:')
    bot.send_message(message2.chat.id,decrypter(message2.text))


bot.polling(none_stop=True)