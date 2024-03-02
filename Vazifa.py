


# from collections import namedtuple

# Kitob = namedtuple('Kitob', ['nomi', 'muallifi', 'narxi'])

# kitob1 = Kitob(nomi='Matnlar olami', muallifi='Alberto Manguel', narxi=25.99)
# kitob2 = Kitob(nomi='Sherlock Holmes', muallifi='Arthur Conan Doyle', narxi=15.50)

# print(kitob1.nomi)  
# print(kitob2.muallifi) 
# print(kitob1.narxi)  
# ----------------------------------------------------------------------------

from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7135056688:AAGl33feySkX5E-ziFdHhBiKACWLrB5xR9o')

@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    print(chat_id)
    bot.send_message(chat_id, f"Assalomu alaykum {full_name}")

@bot.message_handler(content_types=["text", "photo"])
def get_text(message: Message):
    chat_id = message.chat.id
    text = message.text
    # bot.send_message(chat_id, text)
    bot.copy_message(-4134731291, chat_id, message.message_id)

@bot.message_handler(content_types=["video"])
def get_video(message: Message):
    chat_id = message.chat.id
    video = message.video.file_id
    bot.copy_message(-4134731291, chat_id, message.message_id)

@bot.message_handler(content_types=["animation"])
def get_animation(message: Message):
    chat_id = message.chat.id
    animation = message.animation.file_id
    bot.copy_message(-4134731291, chat_id, message.message_id)

bot.polling()
