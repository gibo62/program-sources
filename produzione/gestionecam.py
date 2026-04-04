#!/usr/bin/python
import cgi
import datetime
import logging
import os
#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "../../logs/gestionecam.log",
                    filemode = "a",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()
def attiva(comando):
    if comando=="attivavideo":
		os.system("/home/gb-home/scripts/riavviastreaming.sh video")
        logger.info("Attiva codice Video")
        return """
<div align="center">

<div id="tabla" style="overflow: hidden;">

    <script src="https://cdn.jsdelivr.net/npm/p2p-media-loader-core@latest/build/p2p-media-loader-core.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/p2p-media-loader-hlsjs@latest/build/p2p-media-loader-hlsjs.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/clappr@latest"></script>
<table style="width: 640px;margin-top:20px;"><tbody>
<tr>  <td align="center">
 <!--  
<iframe width="640" height="415" src="https://www.youtube.com/embed/fsZ2nC-Ffvc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
-->

 <!--  QUESTO E' il BLOCCO DEL VIDEO ORIGINALE DI VALME.NET-->
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
 <!--  
  FINE BLOCCO DEL VIDEO ORIGINALE DI VALME.NET
-->

    <!--  BLOCCO VIDEO CHE NON ERA USATO - COMMENTATO E NON ELIMINATO PERCHE'... BOH!
            NON ABILITARE E NON TOGLIERE IL COMMENTO 

    <video id="example_video_1" class="video-js vjs-default-skin vjs-big-play-centered" controls autoplay preload="auto" data-setup='{"fluid": false}' width="480" height="360">
        <source src="https://erosvm3.indigitaleweb.com/live_valme/valme.stream/playlist.m3u8" type="application/x-mpegURL">

     <p class="vjs-no-js">To view this video please enable JavaScript, and consider upgrading to a web browser that <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a></p>
        
       
    </video>-->

</td> </tr>
</tbody></table>

</div>


<center>
<div style="text-align:center: margin-top:35px"> <a href="https://appoggio.nsvalme.cloud/nsvalme/livevideo/Livevideo-NostraSignoradiValme-youtube.html" target="_blank">ATTENZIONE: Clicca qui  se non riesci a vedere la Telecamera</a> </div>
</center></div>
"""
    if comando=="attivaimmagine" and datetime.datetime.now().month == 7:
		os.system("/home/gb-home/scripts/riavviastreaming.sh immagine")
        logger.info("Attiva codice Immagine - Luglio")
        return """
<div align="center">
<p></p>
<center>
    <img border="0" src="https://blogger.googleusercontent.com/img/a/AVvXsEisQCRfOOi7OsV4c2CLr6VGgKupQFvYsAyTLMvWxe3eGuhb_U8cdgitXOF4NZqWaQdAIHFw5l_ZMtRac3zrOeoQZ_KFk_6U5FeJQtIwj-hkPTWQYzS2irsVdxHoKyhtl-CV_J_KbRpf4p1oYa8qHVcm14nWn5lpvp4PDRfrI_vGcVfcQxxiY76bbjrt=s16000" width="640" height="400" valme_date="july" />
</center></div>
"""
    
    elif comando=="attivaimmagine" and datetime.datetime.now().month == 8:
		os.system("/home/gb-home/scripts/riavviastreaming.sh immagine")
        logger.info("Attiva codice Immagine - Agosto")
        return """
<div align="center">
<p></p>
<center>
    <img border="0" src="https://blogger.googleusercontent.com/img/a/AVvXsEjHdDwjnTahpkOJtst1NXjo_QARwQiwo8WB38GnkyF5Et1EYRYP9WwQ9zOunFTIhDEW0yMrEAKMfzPuwfe1dilWEipSq9i1rDsmGO0qvzkRKeoNCS_DeptjKONunFfCLm1fCH6dBKdYTORkr3V5vuVbSV-DUina-ObJ0X_8ech3SGmhbDBKuTCBYhgF=s16000" width="640" height="400" valme_date="august" />
</center></div>
"""
        
    else:
        logger.info("Attiva codice Immagine - No Luglio - No Agosto")
		os.system("/home/gb-home/scripts/riavviastreaming.sh immagine")
        return """
<div align="center">
<p></p>
<center>
    <img border="0" src="https://blogger.googleusercontent.com/img/a/AVvXsEgbpN0VJmm27HoRRpy8GYoAknXwtJN9BdKubZPYONIsSeZcyutc21xnnbWOV2WIXS1cNUzMDMz9X0fpYknrVE3RkrR6JFqq9wh60kyWr3yzItsiMyHHq4SghXFHBklADWi5_DfTwv7R5CT3zz6yhZbV0Tt-MUKRWbW76WPcTPzuNlyjBc8uLmsDUfsh=s16000" width="640" height="400"  valme_date="normal" />
</center></div>
"""



form = cgi.FieldStorage()
print "Content-type: text/html" 
print 
print "<HTML><HEAD></HEAD><BODY>" 
comando=form.getvalue('comando')
f = open('../disattiva.txt')
content = f.read()
f.close
if "dis-off" in content:
    logger.info("Automatismo Abilitato")
    Html_file= open("../embed_homepage.html","w")
    Html_file.write(attiva(comando))
    Html_file.close()
    logger.info("Pagina Embed_homepage.html creata")
    print comando
    print "</BODY></HTML>"
else:
    logger.info("Automatismo Disabilitato: Pagina Embed_homepage_spa.html non sovrascritta")
    print "Automatismo Disabilitato: Pagina Embed_homepage_spa.html non sovrascritta"
    print "</BODY></HTML>"
