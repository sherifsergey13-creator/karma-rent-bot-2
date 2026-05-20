import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = telebot.types.KeyboardButton("🏍 Аренда байка")
    btn2 = telebot.types.KeyboardButton("💰 Цены")
    btn3 = telebot.types.KeyboardButton("📞 Поддержка")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)

    bot.send_message(
        message.chat.id,
        "🏍 Добро пожаловать в KARMA RENT",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    if message.text == "🏍 Аренда байка":
        bot.send_message(message.chat.id, "Список байков скоро появится")

    elif message.text == "💰 Цены":
        bot.send_message(message.chat.id, "Цены скоро появятся")

    elif message.text == "📞 Поддержка":
        bot.send_message(message.chat.id, "@karma_support")

print("Бот запущен...")
bot.infinity_polling()
from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web).start()
