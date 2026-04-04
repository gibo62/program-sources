#!/usr/bin/python3
import cgi
import datetime
import logging
#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "/websites/sanbartolome/logs/gestionecam.log",
                    filemode = "a",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()
def attiva(comando,forza):
    logger.info(forza)
    f = open('../funzione.txt', "w")
    if comando=="attivavideo":
        logger.info("Attiva Trasmissione Video")
        f.write("video\n")
        if forza == "yes":
            f.write("forza\n")
    if comando=="attivaimmagine":
        logger.info("Attiva Trasmissione Immagine")
        f.write("immagine\n")
        if forza == "yes":
            f.write("forza\n")
    f.close

form = cgi.FieldStorage()
print ("Content-type: text/html") 
print ("")
print ("<HTML><HEAD></HEAD>")
print ('<meta name="viewport" content="width=device-width, initial-scale=1">')
print ('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">')
print ("<BODY>")
comando=form.getvalue('comando')
#comando="attivavideo"
forza=form.getvalue('force')
f = open('../disattiva.txt')
content = f.read()
f.close
if "dis-off" in content:
    logger.info("Automatismo Abilitato")
    attiva(comando,forza)
    print (comando)
    print ("</BODY></HTML>")
else:
    logger.info("Automatismo Disabilitato: Comando non eseguito")
    print ("Automatismo Disabilitato: comando non eseguito")
    print ("</BODY></HTML>")
	


