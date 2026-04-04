#!/usr/bin/python3
import cv2
import os
import sys
import datetime
import urllib3
import requests
import socket

http=urllib3.PoolManager()
def esegui(comando):
        s = http.request("GET",comando)
        print(comando)

print (len(sys.argv))
if len(sys.argv) == 3:
	nome_script, sito, ecco= sys.argv
	forza =True
elif len(sys.argv) == 2:
	nome_script, sito = sys.argv
	forza=False
else:
	print("Errore di sintassi. La sintassi del comando e': nome_programma (host) [f] f=force")
	sys.exit()

print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M "),"sito: ",sito)
print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M "),"forza: ",forza)

if sito=="sanpietroapostolo":
	url="rtsp://root:sanpietroapostolo@sanpietroapostolo.nsvalme.cloud:554/axis-media/media.amp"
	ifttt="https://maker.ifttt.com/trigger/notifica_sanpietroapostolo/with/key/cJSX_GyJ6VIECJvK6c4Eap?value1="

if sito=="nsvalme":
        url="rtsp://root:nsvalme@webcam.nsvalme.cloud:554/axis-media/media.amp"
        ifttt="https://maker.ifttt.com/trigger/control_nsvalme/with/key/cJSX_GyJ6VIECJvK6c4Eap?value1="
#        ifttt="https://webhook.homey.app/65f197b6051ba009ecc3cdc9/whatsappvalme?tag="

if sito=="sanbartolome":
        url="rtsp://root:Bartolo2021@webcam.sanbartolome.nsvalme.cloud:554/axis-media/media.amp"
        ifttt="https://maker.ifttt.com/trigger/control_bartolomeo/with/key/cJSX_GyJ6VIECJvK6c4Eap?value1="

#Below code will capture the video frames and will sve it a folder (in current working directory)
#video path
cap = cv2.VideoCapture(url)
count = 0
#while(cap.isOpened()):
ret, frame = cap.read()
print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M "),"frame: ",ret)

if ret:
	if forza:
        	esegui (ifttt+"Webcam%20Operativa")
else:
        esegui (ifttt+"Webcam%20NON%20Operativa")
cap.release()
cv2.destroyAllWindows()

