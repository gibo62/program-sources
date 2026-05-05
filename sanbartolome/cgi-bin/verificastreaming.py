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
logpath="../../logs/verificaurl.log"
#logpath="/websites/appoggio/logs/verificaurl.log"
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

with urllib.request.urlopen('https://www.youtube.com/@ParroquiaSanBartolomeySanE-g8y/live') as response:
	html = str(response.read())
	html=str(html.encode('ascii','ignore'))

x = html.find(caption)
if caption in html:
    urllib.request.urlopen('https://maker.ifttt.com/trigger/control_bartolomeo/with/key/cJSX_GyJ6VIECJvK6c4Eap?value2=SANBARTOLOME&value1=Transmision%20Youtube%20Activa')
    logger.info("Streaming su Youtube Attivo")
    print ("Transmision Youtube Activa")
    print ("</BODY></HTML>")
else:
    urllib.request.urlopen('https://maker.ifttt.com/trigger/control_bartolomeo/with/key/cJSX_GyJ6VIECJvK6c4Eap?value2=SANBARTOLOME&value1=Transmision%20Youtube%20Interrumpida')
    logger.info("Streaming su Youtube Interrotto")
    print ("Transmision Youtube Interrumpida")
    print ("</BODY></HTML>")
#file = open ("/home/gb-home/scripts/videosi","w")
#file.write (html)
#file.close()

