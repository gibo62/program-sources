#!/usr/bin/python

import os
import platform
import datetime
import time
import sys
import urllib

def esegui(comando):
        s = urllib.urlopen(comando)
        print comando

if len(sys.argv) < 2:
        print("Errore di sintassi. La sintassi del comando e': nome_programma (host) [f] f=force")
        sys.exit()
intervallo=20
telefono="3351563802"
if len(sys.argv) == 2:
	nome_script, sito = sys.argv
	forza="n"
if len (sys.argv) == 3:
        nome_script, sito, forza = sys.argv
response1 = 0
now = datetime.datetime.now()
nomefile="/home/gb-home/scripts/"+sito+".txt"

try:
	response1 = os.system("ping -c 1 " + sito + "> /home/gb-home/scripts/testingping.log")
except:
	response1 = 1

if forza != "f":
	try:
  		file = open (nomefile, "r")
		responseold = int(file.read())
  		file.close()
	except:
  		responseold = -1
else:
	print "force mode"	
	responseold = -1

print now.strftime("%Y-%m-%d %H:%M"),responseold, response1,

# Scrivi stato
file = open(nomefile, "w")
file.write(str(response1))
file.close()

# Prepare actual message
if response1 > 0:
        body=sito+" Connection DOWN"
else:
        body=sito+" Connection UP"
if response1 != responseold:
	now =datetime.datetime.now()
	esegui ("https://maker.ifttt.com/trigger/NotificaGIBO/with/key/cJSX_GyJ6VIECJvK6c4Eap?value2="+now.strftime("%Y-%m-%d %H:%M ")+" Sito: "+body)
        print "Cambio Stato ",
print body
