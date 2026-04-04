#!/usr/bin/python3
nomefile="/home/gb-home/scripts/youtubevalme"
import urllib.request
import sys
forza="n"
caption="html5-video-player"
if len(sys.argv) == 2:
        nome_script, forza = sys.argv

with urllib.request.urlopen('https://www.youtube.com/c/ValmeNet/live') as response:
	html = str(response.read())
	html=str(html.encode('ascii','ignore'))

	file = open("/home/gb-home/scripts/youtubevalme2", "w")
	file.write(html)
	file.close()
	print (html)

try:
	file = open (nomefile, "r")
	statoold = file.read()
	file.close()
	if forza != "n":
		statoold='n/a'
except:
        statoold='n/a'
x = html.find(caption)
print (html[x:x+len(caption)])
print (caption in html)
if caption in html:
	if statoold != 'on':
		urllib.request.urlopen('https://maker.ifttt.com/trigger/control_nsvalme/with/key/cJSX_GyJ6VIECJvK6c4Eap?value1=Streaming%20YouTube%20Attivo&value2=NS%20VALME')
		urllib.request.urlopen('https://webhook.homey.app/65f197b6051ba009ecc3cdc9/whatsappvalme?tag=WebcamValme:Streaming%20YouTube%20Attivo')
		youtubevalme='on'
		file = open(nomefile, "w")
		file.write(youtubevalme)
		file.close()
else:
	if statoold != 'off':
		urllib.request.urlopen('https://maker.ifttt.com/trigger/control_nsvalme/with/key/cJSX_GyJ6VIECJvK6c4Eap?value1=Streaming%20YouTube%20Disattivo&value2=NS%20VALME')
		urllib.request.urlopen('https://webhook.homey.app/65f197b6051ba009ecc3cdc9/whatsappvalme?tag=WebcamValme:Streaming%20YouTube%20Disattivo')
		youtubevalme='off'
		file = open(nomefile, "w")
		file.write(youtubevalme)
		file.close()

#file = open ("/home/gb-home/scripts/videosi","w")
#file.write (html)
#file.close()

