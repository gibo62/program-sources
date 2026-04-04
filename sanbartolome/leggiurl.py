#!/usr/bin/python3
nomefile="/home/scripts/youtubesanbartolome"
import urllib.request
import sys
import re
forza="n"
caption="html5-video-player"
if len(sys.argv) == 2:
        nome_script, forza = sys.argv

#with urllib.request.urlopen('https://sanbartolome.nsvalme.cloud/eventostream.html') as response:
with urllib.request.urlopen('https://www.youtube.com/@ParroquiaSanBartolomeySanE-g8y/live') as response:
#with urllib.request.urlopen('https://www.youtube.com/embed/AGXGwYiRqDY') as response:
    html = str(response.read())
#    print (html)
#    x = html.find('source_ve_path')
#    print (x)
#   video='https://www.youtube.com/watch?v=live_stream&source_ve_path='+html[x+21:x+21+8]
#    print (video)

#    html = str(urllib.request.urlopen(video).read())
    html=str(html.encode('ascii','ignore'))

    file = open("/home/scripts/youtubesanbartolomepagina2", "w")
    file.write(html)
    file.close()


    print (html)
#   print(html)
#    x=html.find('questo')
#    print (x)
#    print (html[x:x+60])

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
		urllib.request.urlopen('https://maker.ifttt.com/trigger/control_bartolomeo/with/key/cJSX_GyJ6VIECJvK6c4Eap?value2=SANBARTOLOME&value1=Transmision%20Youtube%20Activa')
		urllib.request.urlopen('https://webhook.homey.app/65f197b6051ba009ecc3cdc9/whatsappvalme?tag=Sanbartolome:Streaming%20YouTube%20Attivo')
		#urllib.request.urlopen('https://maker.ifttt.com/trigger/control_bartolomeo/with/key/cJSX_GyJ6VIECJvK6c4Eap?value2=SANBARTOLOME&value1=Transmision%20Youtube%20Interrumpida')
		youtubesite='on'
		file = open(nomefile, "w")
		file.write(youtubesite)
		file.close()
else:
	if statoold != 'off':
#		urllib.request.urlopen('https://maker.ifttt.com/trigger/control_bartolomeo/with/key/cJSX_GyJ6VIECJvK6c4Eap?value2=SANBARTOLOME&value1=Transmision%20Youtube%20Activa')
		urllib.request.urlopen('https://maker.ifttt.com/trigger/control_bartolomeo/with/key/cJSX_GyJ6VIECJvK6c4Eap?value2=SANBARTOLOME&value1=Transmision%20Youtube%20Interrumpida')
		urllib.request.urlopen('https://webhook.homey.app/65f197b6051ba009ecc3cdc9/whatsappvalme?tag=Sanbartolome:Streaming%20YouTube%20Disattivo')
		youtubesite='off'
		file = open(nomefile, "w")
		file.write(youtubesite)
		file.close()



