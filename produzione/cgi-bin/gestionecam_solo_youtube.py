#!/usr/bin/python
import cgi
import datetime
import logging
import time
import urllib.request

#logpath="../../logs/gestionecam.log"
logpath="/websites/appoggio/logs/gestionecam.log"
#pathsito="/websites/appoggio/www/"
pathsito="../"
#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = logpath,
                    filemode = "a",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()

def esegui(comando):
    u = urllib.request.urlopen(comando)
    logger.info(comando)

def attiva(comando,forza):
    logger.info(forza)
    if comando=="attivavideo":
        logger.info("Attiva codice Video")
#        esegui("https://maker.ifttt.com/trigger/control_nsvalme/with/key/cJSX_GyJ6VIECJvK6c4Eap?value1=Attiva%20Video")
#        esegui("https://webhook.homey.app/65f197b6051ba009ecc3cdc9/ipcamvalme/ON")
        esegui ("https://webhook.homey.app/65f197b6051ba009ecc3cdc9/valme?tag=ON")
        f = open(pathsito+'funzione.txt', "w")
        f.write("video\n")
        if forza == "yes":
            f.write("forza\n")
        f.close
        return """
<div align="center">

<div id="tabla" style="overflow: hidden;">

    <script src="https://cdn.jsdelivr.net/npm/p2p-media-loader-core@latest/build/p2p-media-loader-core.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/p2p-media-loader-hlsjs@latest/build/p2p-media-loader-hlsjs.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/clappr@latest"></script>
<table style="width: 640px;margin-top:20px;"><tbody>
<tr>  <td align="center">
 
<iframe width="640" height="415" src="https://www.youtube.com/embed/live_stream?channel=UCICCeSk_8vOJ0kjD7nNppcg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


 <!--  QUESTO E' il BLOCCO DEL VIDEO ORIGINALE DI VALME.NET
 
 <div id="player" width="640px" height="360px"></div>
    <script>
        if (p2pml.hlsjs.Engine.isSupported()) {
            var engine = new p2pml.hlsjs.Engine();

            var player = new Clappr.Player({
                parentId: "#player",
                source: "https://erosvm3.indigitaleweb.com/live_valme/valme.stream/playlist.m3u8",
                mute: false,
                autoPlay: true,
                playback: {
                    hlsjsConfig: {
                        liveSyncDurationCount: 7,
                        loader: engine.createLoaderClass()
                    }
                }
            });

            player.resize({height: 360, width: 640})
            p2pml.hlsjs.initClapprPlayer(player);
        } else {
            document.write("Not supported :(");
        }
    </script>
  
  FINE BLOCCO DEL VIDEO ORIGINALE DI VALME.NET
-->

</td> </tr>
</tbody></table>

</div>


<center>
<div style="text-align:center: margin-top:35px"> <a href="https://appoggio.nsvalme.cloud/nsvalme/livevideo/Livevideo-NostraSignoradiValme-youtube.html" target="_blank">ATTENZIONE: Clicca qui  se non riesci a vedere la Telecamera</a> </div>
</center></div>
"""
    if comando=="attivaimmagine":
        logger.info("Attiva codice Immagine - Luglio")
        esegui ("https://webhook.homey.app/65f197b6051ba009ecc3cdc9/valme?tag=OFF")
 #       esegui("https://maker.ifttt.com/trigger/control_nsvalme/with/key/cJSX_GyJ6VIECJvK6c4Eap?value1=Attiva%20Immagine%20(Luglio)")
        f = open(pathsito+'funzione.txt', "w")
        f.write("immagine\n")
        if forza == "yes":
            f.write("forza\n")
        f.close
        return """
<div align="center">
<p></p>
<center>
    <img border="0" src="https://appoggio.nsvalme.cloud/nsvalme/immagine-attiva.png" width="640" height="400" valme_date="normal" />
</center></div>
"""



form = cgi.FieldStorage()
print ("Content-type: text/html\n\n")
print
print ("<HTML><HEAD></HEAD><BODY>") 
comando=form.getvalue('comando')
forza=form.getvalue('force')
modo= pathsito+"disattiva.txt"
#comando="attivavideo"
#modo="/websites/appoggio/www/disattiva.txt"
f = open(modo)
content = f.read()
f.close
if "dis-off" in content:
    logger.info("Automatismo Abilitato")
    Html_file= open(pathsito+"embed_homepage.html","w")
    Html_file.write(attiva(comando,forza))
    Html_file.close()
    logger.info("Pagina Embed_homepage.html creata")
    print (comando)
    print ("</BODY></HTML>")
else:
    logger.info("Automatismo Disabilitato: Pagina Embed_homepage_spa.html non sovrascritta")
    print ("Automatismo Disabilitato: Pagina Embed_homepage_spa.html non sovrascritta")
    print ("</BODY></HTML>")
