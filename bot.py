#-*- coding: utf-8 -*-
import telebot

TOKEN = "987421062:AAFIGRX3jkkzJKBtXSE4dp6BhGdOH10wTuU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
	user_markup=telebot.types.ReplyKeyboardRemove()
	bot.send_message(message.from_user.id,"Наберіть '/go' для початку роботи",reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def handle_text_message(message):
	user_markup = telebot.types.ReplyKeyboardRemove()
	bot.send_message(message.from_user.id, "/start - Почати заново\n/go - посилання запиту\n/lol - Написати Артемкові)", reply_markup=user_markup)

@bot.message_handler(commands=['go'])
def handle_start(message):
	user_markup=telebot.types.ReplyKeyboardMarkup(1,0)
	user_markup.row('Перший', 'Другий')
	bot.send_message(message.from_user.id, "За який тиждень Вас цікавить розклад?", reply_markup=user_markup)

week=0
day=0
@bot.message_handler(content_types=['text'])
def handle_text_message(message):
	if message.text == "Перший":
		week=1

		bot.send_message(message.chat.id,"Ви обрали розклад на перший тиждень")
		user_markup = telebot.types.ReplyKeyboardMarkup(1,0)
		user_markup.row('Понеділок','Вівторок')
		user_markup.row('Середа' )
		user_markup.row('Четвер',"П'ятниця" )
		bot.send_message(message.from_user.id,f"НА який день ви хочете побачити розклад?{week}",reply_markup=user_markup)

	elif message.text == 'Другий':

		week=2

		bot.send_message(message.chat.id, "Ви обрали розклад на другий тиждень")
		user_markup = telebot.types.ReplyKeyboardMarkup(1,0)
		user_markup.row('Понеділок', 'Вівторок')
		user_markup.row('Середа')
		user_markup.row('Четвер', "П'ятниця")
		bot.send_message(message.from_user.id, f"На який день ви хочете побачити розклад? {week}", reply_markup=user_markup)
@bot.message_handler(content_types1=['text'])
def handle(message):
	if message.text=='Вівторок' and week==1:
		bot.send_message(message.from_user.id, f"i love bublik")











bot.polling(none_stop=True)