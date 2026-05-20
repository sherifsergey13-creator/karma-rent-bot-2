import os
import threading
from flask import Flask
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "KARMA RENT bot is running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

@bot.message_handler(commands=["start"])
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
        bot.send_message(
            message.chat.id,
            "Доступные байки скоро появятся."
        )

    elif message.text == "💰 Цены":
        bot.send_message(
            message.chat.id,
            "💰 Цены скоро появятся."
        )

    elif message.text == "📞 Поддержка":
        bot.send_message(
            message.chat.id,
            "📞 Поддержка: @karma_support"
        )

    else:
        bot.send_message(
            message.chat.id,
            "Выберите кнопку в меню 👇"
        )

print("Бот запущен...")

threading.Thread(target=run_web).start()

bot.infinity_polling()
