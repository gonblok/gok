from datetime import date
from pycoingecko import CoinGeckoAPI
import requests as r
import time
def cek():
	today = date.today()
	d3 = today.strftime("%m/%d/%y")
	print(type(d3))
	print(d3)
	cg = CoinGeckoAPI()
	print("Trending Koin di CoinGecko\n")
	koin = cg.get_search_trending()
	koinl = koin.get("coins")
	r.get("https://api.telegram.org/bot5153674664:AAGIf3UvyN4cA1cLsvakQNmQSY7DUsEMfss/sendMessage?chat_id=2071025459&text=DAFTAR KOIN TRENDING DI COINGECKO {}".format(d3))
	for i in range(7):
		c = i+1
		hasil =str(c)+"."+koinl[i].get("item")['name']
		print(hasil)
		r.get("https://api.telegram.org/bot5153674664:AAGIf3UvyN4cA1cLsvakQNmQSY7DUsEMfss/sendMessage?chat_id=2071025459&text={}".format(hasil))

while True:
	cek()
	time.sleep(900)
#r.get("https://api.telegram.org/bot5153674664:AAGIf3UvyN4cA1cLsvakQNmQSY7DUsEMfss/sendMessage?chat_id=2071025459&text=---------------------------------------------------------------------------------------")
