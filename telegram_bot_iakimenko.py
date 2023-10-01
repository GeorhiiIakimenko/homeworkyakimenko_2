import requests
import telebot
from telebot import types

TOKEN = '5957462664:AAEPF5zXxyZx9Lqe-1pNXsEyBXSisLU14ig'
WEATHER_API_KEY = '499b8a63224a3c6f7afa08d99009fb21'
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=ua"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привіт! Напиши мені назву міста в Україні, і я повідомлю тобі погоду у ньому, або вибери місто зі списку нижче.")

    markup = types.InlineKeyboardMarkup()
    cities = ["Київ", "Харків", "Одеса", "Львів", "Дніпро"]
    for city in cities:
        button = types.InlineKeyboardButton(text=city, callback_data=city)
        markup.add(button)
    bot.send_message(message.chat.id, "Оберіть місто:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        city = call.data
        send_weather_for_city(call.message, city)


@bot.message_handler(content_types=['text'])
def send_weather(message):
    city = message.text
    send_weather_for_city(message, city)


def send_weather_for_city(message, city):
    try:
        result = requests.get(WEATHER_URL.format(city, WEATHER_API_KEY)).json()
        weather_description = result['weather'][0]['description']
        temperature = result['main']['temp']
        response_text = f'Погода у місті {city}:\n{weather_description.capitalize()}\nТемпература: {temperature}°C'
        bot.send_message(message.chat.id, response_text)
    except:
        bot.send_message(message.chat.id, "Вибачте, я не зміг знайти інформацію про погоду для цього міста.")


bot.polling()
