import random
import telebot
from config import TOKEN
bor = telebot.telebot(TOKEN)
def password(n):
    simvol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    p = ""
    for i in range (n):
        p += random.choice(simvol)
    return(p)

def password2(n):
    simvol = "+-:*=1234567890"
    p = ""
    for i in range (n):
        p += random.choice(simvol)
    return(p)

def password3(n):
    simvol = "/hello,/heh,/heh 10 и т.д,/he,/random,/gen_pass,/mathematik_example"
    p = ""
    for i in range (n):
        p += random.choice(simvol)
    return(p)
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=['random'])
def send_heh(message):
   bot.reply_to(message, f"твоё число:{random.randint(1,10)}")

@bot.message_handler(commands=['gen_pass'])
def send_heh(message):
    bot.reply_to(message, f"твой пароль:{password(8)}")

@bot.message_handler(commands=['mathematical_example'])
def send_heh(message):
    bot.reply_to(message, f"твой математический пример:{password2(8)}")

@bot.message_handler(commands=['help_helping'])
def send_heh(message):
    bot.reply_to(message, f"Все функции:{password3(8)}")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text) 
    
@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)    
# Запуск бота
bot.polling()