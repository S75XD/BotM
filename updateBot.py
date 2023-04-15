''' By SaLeH insta @8_wvu '''

import telebot,requests

bot = telebot.TeleBot("6042858498:AAGJu5gdQc3ciEpQB9iPUUUk12qFOUQJKH0", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	userid = (f"{message.from_user.id}")

	idfile = open("id.txt","r").read()
	if userid in idfile:
		bot.send_message(message.chat.id,"hello (:")

	else:
	  with open("id.txt","a") as kl :
	    kl.write(f"{userid}\n")
	    bot.send_message(message.chat.id,"hello (:")

def chak():
	response = requests.get("https://raw.githubusercontent.com/S75XD/BotM/main/package.json")
	version = (response.json()["version"])
	# oldVersion = open("oldVersion.txt",'a').read()
	with open("oldVersion.txt","a") as oldVersion :
		oldVersion.write(f"{version}\n")

	if version!=oldVersion:
		
		chats = open('id.txt','r')
		for chat in chats:
			bot.send_message(chat,f"New version available {version}")


chak()

# while True:
# 	try:
# 		bot.polling(none_stop=True, timeout=90)
# 	except Exception as e:
# 		time.sleep(5)
# 		continue
bot.polling(none_stop=True, timeout=90)