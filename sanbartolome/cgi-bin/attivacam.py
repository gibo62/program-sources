#!/usr/bin/python3
import cgi
from urllib.request import urlopen
import logging
import requests

#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "/websites/sanbartolome/logs/attivacam.log",
                    filemode = "a",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()

#Testing our Logger

def esegui(urlpath):
	with urlopen(urlpath) as response:
		s=response.read()
	logger.info(urlpath)

form = cgi.FieldStorage()
print ("Content-type: text/html") 
print ("")
print ("<HTML><HEAD></HEAD>")
print ("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
print ("<link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">")
print ("<BODY>")
print ("<div class=\"w3-container w3-center\">")
print ("<table class=\"w3-table w3-striped w3-border\">")
print ("<tr>")
print ("<th colspan=\"5\">")
print ("<div class=\"w3-round-xxlarge w3-orange w3-center style=\"text-shadow:1px 1px 0 #444\"\">")
print ("<h1>Webcam San Bartolome'</h1>")
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
f.close()  # chiudiamo il file
path="https://sanbartolome.nsvalme.cloud/cgi-bin/gestionecamyoutube.py?force=yes&comando="+comando
esegui(path)
logger.info(path)
f = open('../disattiva.txt', 'w')
if disattiva=="on":
    print ("<th style=\"color: red\">Desactivar</th>")
    logger.info("attivata funzione Manuale")
    f.write('dis-on\n')
else:
    print ("<th style=\"color: green\">AUTOMATICO</th>")
    logger.info("attivata funzione Automatica")
    f.write('dis-off\n')
f.close()  # chiudiamo il file
print ("</tr><tr>")
print ("</tr><tr>")
print ("<th class=\"w3-right\">Funcion:</th>")
if comando=="attivaimmagine":
    print ("<th style=\"color: blue\">IMAGEN ACTIVADA esperas unos 2 minutos para el cambio</th>")
    logger.info("Visualizzazione Immagine")
else:
    print ("<th style=\"color: blue\">VIDEO ACTIVADO esperas unos 2 minutos para el cambio</th>")
    logger.info("Visualizzazione Video")
print ("</tr></table></div>")
print ("</BODY></HTML>")

