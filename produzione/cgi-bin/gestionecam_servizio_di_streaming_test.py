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

    <table style="width: 640px; margin-top:20px;">
      <tbody>
        <tr>
          <td align="center">

            <!-- Video.js CSS (CDN) -->
            <link rel="stylesheet" href="https://vjs.zencdn.net/8.10.0/video-js.css">

            <!-- PLAYER VIDEO -->
            <video
              id="example_video_1"
              class="video-js vjs-default-skin vjs-big-play-centered"
              controls
              autoplay
              muted
              playsinline
              preload="auto"
              width="640"
              height="360"
            >
              <source src="http://erosvm3.indigitaleweb.com/live_valme/valme.stream/playlist.m3u8" type="application/x-mpegURL">
              <p class="vjs-no-js">
                To view this video please enable JavaScript, and consider upgrading to a web browser that
                <a href="http://videojs.com/html5-video-support/" target="_blank" rel="noopener">supports HTML5 video</a>
              </p>
            </video>

            <!-- Video.js JS (CDN) -->
            <script src="https://vjs.zencdn.net/8.10.0/video.min.js"></script>

            <script>
              videojs("example_video_1", {
                autoplay: true,
                muted: true,
                controls: true,
                preload: "auto",
                liveui: true
              });
            </script>

            <!--  BLOCCO VIDEO CHE NON ERA USATO - COMMENTATO E NON ELIMINATO PERCHE'... BOH!
                  NON ABILITARE E NON TOGLIERE IL COMMENTO

            <video id="example_video_1_old" class="video-js vjs-default-skin vjs-big-play-centered" controls autoplay preload="auto" data-setup='{"fluid": false}' width="640" height="360">
                <source src="https://erosvm3.indigitaleweb.com/live_valme/valme.stream/playlist.m3u8" type="application/x-mpegURL">
                <p class="vjs-no-js">To view this video please enable JavaScript, and consider upgrading to a web browser that <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a></p>
            </video>
            -->

          </td>
        </tr>
      </tbody>
    </table>

  </div>

  <center>
    <div style="text-align:center; margin-top:35px">
      <a href="https://appoggio.nsvalme.cloud/nsvalme/livevideo/Livevideo-NostraSignoradiValme-youtube.html" target="_blank" rel="noopener">
        ATTENZIONE: Clicca qui se non riesci a vedere la Telecamera
      </a>
    </div>
  </center>

</div>
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
