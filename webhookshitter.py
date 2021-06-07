#imports:
from discord_webhook import DiscordWebhook
import time
def logo():
	print("              _     _                 _          _     _ _   _            ")
	print("             | |   | |               | |        | |   (_) | | |           ")
	print("__      _____| |__ | |__   ___   ___ | | __  ___| |__  _| |_| |_ ___ _ __ ")
	print("\ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / / __| '_ \| | __| __/ _ \ '__|")
	print(" \ V  V /  __/ |_) | | | | (_) | (_) |   <  \__ \ | | | | |_| ||  __/ |   ")
	print("  \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |___/_| |_|_|\__|\__\___|_|   ")
	print("by SpezialK#4807")
def main():
	#who and what will be spammed
	logo()
	target =input("webhook link: " )
	msg = input("here your spammer msg:  ")
	amount = int(input("the amount of msgs: "))
	n = 0
	while n < amount:
		tsleep = randint(1 , 3 )
		webhook = DiscordWebhook(url=target, content=msg)
		time.sleep(tsleep)
		response = webhook.execute()
		n = n+1
main()
#external modules needed: discord webhook
#installed with the following comand :
#pip install discord-webhook 
