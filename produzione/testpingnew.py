#!/usr/bin/python

import socket

import os
import platform
import datetime
import time
import sys
import urllib.request
import requests


def trova_ip_sito(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        print(f"Il sito {dominio} ha indirizzo IP: {ip}")
        return ip
    except socket.gaierror:
        print(f"Impossibile trovare l'IP per {dominio}")
        return None


def esegui(comando):
        s = urllib.request.urlopen(comando)
        print (comando)

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
nomefileip="/home/gb-home/scripts/"+sito+"ip.txt"
try:
	response1 = socket.gethostbyname(sito)
	body =sito+"%20Nuovo%20IP:%20"+response1
except:
	response1 = "N/A"
	body =sito+"%20Nuovo%20IP:%20Not%20Correct"	

if forza != "f":
	try:
		file = open (nomefileip, "r")
		responseold = file.read()
		file.close()
	except:
		responseold = "N/A"
else:
	print ("force mode")
	responseold = "N/A"

# Prepare actual message
# Scrivi stato
file = open(nomefileip, "w")
file.write(str(response1))
file.close()       

if response1 != responseold:
	now =datetime.datetime.now()
#	urllib.request.urlopen('https://maker.ifttt.com/trigger/control_nsvalme/with/key/cJSX_GyJ6VIECJvK6c4Eap?value1='+body+'&value2=NS%20VALME')
	esegui('https://webhook.homey.app/65f197b6051ba009ecc3cdc9/whatsappgibo?tag=%20'+body)
#	esegui ("https://maker.ifttt.com/trigger/NotificaGIBO/with/key/cJSX_GyJ6VIECJvK6c4Eap?value2="+body)
	print ("Cambio IP ",)
print (body, response1, responseold)
