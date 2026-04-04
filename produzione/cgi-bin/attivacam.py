#!/usr/bin/python3
import cgi
import urllib.request
import logging
import requests

#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logpath="/websites/appoggio/logs/attivacam.log"
logging.basicConfig(filename = logpath,
                    filemode = "a",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()

#Testing our Logger

def esegui(urlpath):
	u = urllib.request.urlopen(urlpath)#The url you want to open
	logger.info(urlpath)

url_gestionecam='https://appoggio.nsvalme.cloud/cgi-bin/gestionecam.py?comando='

form = cgi.FieldStorage()
print ("Content-type: text/html") 
print ("")
print ("<HTML><HEAD></HEAD>")
print ('<meta name="viewport" content="width=device-width, initial-scale=1">')
print ('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">')
print ("<BODY>")
print ('<div class="w3-container w3-center">')
print ('<table class="w3-table w3-striped w3-border">')
print ("<tr>")
print ('<th colspan="2">')
print ('<div class="w3-round-xxlarge w3-green w3-center style="text-shadow:1px 1px 0 #444"">')
print ("<h2>Webcam NS Signora di Valme</h2>")
print ("</div>")
print ("</th>")
print ("</tr>")
print ("<tr>")
comando=form.getvalue('comando')
disattiva=form.getvalue('disattiva')
print ("<th class=\"w3-right\">Webcam:</th>")
f = open('../disattiva.txt', 'w')
logger.info("disabilito funzione Manuale")
f.write('dis-off\n')
f.close()  # chiudiamo il fileprint "</tr><tr>"
path='https://appoggio.nsvalme.cloud/cgi-bin/gestionecam.py?force=yes&comando='+comando
logger.info(path)
# response = urllib2.urlopen(path)
f = open('../disattiva.txt', 'w')
if disattiva=="on":
    print ('<th style="color: red">MANUALE</th>')
    logger.info("attivata funzione Manuale")
    f.write('dis-on\n')
else:
    print ('<th style="color: green">AUTOMATICO</th>')
    logger.info("attivata funzione Automatica")
    f.write('dis-off\n')
f.close()  # chiudiamo il fileprint "</tr><tr>"
print ("</tr><tr>")
print ('<th class="w3-right">Funzione:</th>')
if comando=="attivaimmagine":
    esegui(url_gestionecam+comando)
    print ('<th style="color: blue">IMMAGINE ATTIVATA</th>')
    logger.info("Visualizzazione Immagine")
else:
    esegui(url_gestionecam+comando)
    print ('<th style="color: blue">VIDEO ATTIVATO</th>')
    logger.info("Visualizzazione Video")
print ("</tr></table></div>")
print ("</BODY></HTML>")
logger.info("finito")

