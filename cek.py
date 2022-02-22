import os
import telebot
import requests as r
import json

def cek():
  global hargaj
  data = r.get("https://indodax.com/api/tickers")
  data1 = json.loads(data.content.decode('utf-8'))
  harga = 'btc_idr'.replace("_idr",""),data1['tickers']['btc_idr']['last']
  hargaj = '  :  '.join(harga)

API_KEY = '5153674664:AAGIf3UvyN4cA1cLsvakQNmQSY7DUsEMfss'
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['info'])
def info(message):
  cek()
  bot.reply_to(message,hargaj)

bot.polling()
