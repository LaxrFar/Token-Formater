import threading
import random
import json
import time
import easygui
import os
file = easygui.fileopenbox()
TOKENS = open(file,'r').read().splitlines()
count = 0
def formatter(TOKEN):
	len(TOKEN.split(':')) == 4
	splitted = TOKEN.split(':')
	email = f"{splitted[0]}"
	password = f"{splitted[1]}"
	token = f"{splitted[2]}"
	with open(f"output.txt", "a") as f:
		f.write(f"{token}\n")
		f.close()

for TOKEN in TOKENS:threading.Thread(target = formatter,args=(TOKEN,)).start();count +=1
easygui.msgbox(msg=f"{count} TOKENS Formatted", title="TOKEN Formater laxrfar.xyz", ok_button="CLOSE")