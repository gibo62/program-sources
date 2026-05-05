#!/usr/bin/python3

import urllib.request
import sys
import cgi
import datetime
import logging
import time

nomefile="/home/gb-home/scripts/youtubevalme"
forza="n"
caption="html5-video-player"
#logpath="../../logs/verificaurl.log"
logpath="/websites/appoggio/logs/verificaurl.log"
#pathsito="/websites/appoggio/www/"
pathsito="../"
#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = logpath,
                    filemode = "a",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()

print ("Content-type: text/html\n\n")
print
print ("<HTML><HEAD></HEAD><BODY>") 

with urllib.request.urlopen('https://www.youtube.com/c/ValmeNet/live') as response:
	html = str(response.read())
	html=str(html.encode('ascii','ignore'))

try:
x = html.find(caption)
if caption in html:
	urllib.request.urlopen('https://webhook.homey.app/65f197b6051ba009ecc3cdc9/whatsappvalme?tag=WebcamValme:Streaming%20YouTube%20Attivo')
    logger.info("Streaming WebCam Valme Attivo")
    print ("Streaming WebCam Valme Attivo")
    print ("</BODY></HTML>")
else:
	urllib.request.urlopen('https://webhook.homey.app/65f197b6051ba009ecc3cdc9/whatsappvalme?tag=WebcamValme:Streaming%20YouTube%20Disattivo')
    logger.info("Streaming WebCam Valme Disattivo")
    print ("Streaming WebCam Valme Disattivo")
    print ("</BODY></HTML>")
#file = open ("/home/gb-home/scripts/videosi","w")
#file.write (html)
#file.close()

