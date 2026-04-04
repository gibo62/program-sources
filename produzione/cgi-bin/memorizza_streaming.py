#!/usr/bin/python
import cgi
import urllib2
import logging
import os
import platform
import datetime
import time
import sys

#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "../../logs/memorizza_streaming.log",
                    filemode = "a",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()

#Testing our Logger



form = cgi.FieldStorage()
print "Content-type: text/html" 
print 
print "<HTML><HEAD></HEAD>"
print "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
print "<link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">"
print "<BODY>"
print "<div class=\"w3-container w3-center\">"
print "<table class=\"w3-table w3-striped w3-border\">"
print "<tr>"
print "<th colspan=\"5\">"
print "<div class=\"w3-round-xxlarge w3-orange w3-center style=\"text-shadow:1px 1px 0 #444\"\">"
print "<h1>Webcam NS Signora di Valme</h1>"
print "</div>"
print "</th>"
print"</tr>"
print "<tr>"
comando=form.getvalue('comando')
print "<th class=\"w3-right\">Webcam:</th>"
nome_file="/home/nsvalme/nsvalme_"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
path='/usr/bin/ffmpeg1 -rtsp_transport tcp -i rtsp://webcam.nsvalme.cloud:554/axis-media/media.amp -framerate 20 -vcodec copy -codec:a aac -b:a 1288k -ar 44100 -f flv -r 25 '+nome_file
logger.info(path)
response1 = os.system(path)
print "</tr></table></div>"
print "</BODY></HTML>"

