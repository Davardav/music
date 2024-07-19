from logic import DB_Manager
from config import *
from telebot import TeleBot

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот для помощи в музыке из спотифая
""")

@bot.message_handler(commands=['artist'])
def start_command(message):
    bot.send_message(message.chat.id, "Введите псевдоним автора:")
    bot.register_next_step_handler(message, name_artist)

def name_artist(message):
    res = manager.artistss(message.text) 
    bot.send_message(message.chat.id, res)



@bot.message_handler(commands=['id_song'])
def start_command(message):
    bot.send_message(message.chat.id, "Введите id песни:")
    bot.register_next_step_handler(message, name_artist)

def name_artist(message):
    res = manager.get_music_by_id(message.text) 
    bot.send_message(message.chat.id, res)

@bot.message_handler(commands=['name_song'])
def start_command(message):
    bot.send_message(message.chat.id, "Введите имя песни:")
    bot.register_next_step_handler(message, name_artist)

def name_artist(message):
    res = manager.get_music_by_name(message.text) 
    bot.send_message(message.chat.id, res)

@bot.message_handler(commands=['top'])
def start_command(message):
    res = manager.top_popularity() 
    bot.send_message(message.chat.id, res)


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()