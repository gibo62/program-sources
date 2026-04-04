#!/usr/bin/python
import cgi
import datetime
import logging
#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "../../logs/gestionecam.log",
                    filemode = "a",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()
def attiva(comando):
    if comando=="attivavideo":
        logger.info("Attiva codice Video")
        return """
<div align="center">

<div id="tabla" style="overflow: hidden;">

    <script src="https://cdn.jsdelivr.net/npm/p2p-media-loader-core@latest/build/p2p-media-loader-core.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/p2p-media-loader-hlsjs@latest/build/p2p-media-loader-hlsjs.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/clappr@latest"></script>
<table style="width: 640px;margin-top:20px;"><tbody>
<tr>  <td align="center">

<!--  1 - UNCOMMENT THIS LINE TO ACTIVATE YOUTUBE LIVE TRANSMISSION 
<iframe width="686" height="386" src="https://www.youtube-nocookie.com/embed/live_stream?channel=UC08k41lkjJ37v-6k6k-6ZwQ&amp;enablejsapi=1&amp;wmode=opaque&amp;rel=0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
-->

<!--  QUESTO E' il BLOCCO DEL VIDEO ORIGINALE DI VALME.NET  --> 


<div id="player" width="686px" height="386px"></div>
    <script>
        if (p2pml.hlsjs.Engine.isSupported()) {
            var engine = new p2pml.hlsjs.Engine();

            var player = new Clappr.Player({
                parentId: "#player",
                source: "https://erosvm3.indigitaleweb.com/sanbartolomeysanesteban/sanbartolomeysanesteban.stream/playlist.m3u8",
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

 
<!--  FINE BLOCCO DEL VIDEO ORIGINALE DI VALME.NET-->


   

</td> </tr>
</tbody></table>

</div>

</div>
"""
    if comando=="attivaimmagine" and datetime.datetime.now().month == 7:
        logger.info("Attiva codice Immagine - Luglio")
        return """
<div align="center">
<p></p>
<center>
	<img border="0" src="../Fondo-streaming.jpg" width="640" height="400" valme_date="july" />	
</center></div>
"""
    
    elif comando=="attivaimmagine" and datetime.datetime.now().month == 8:
        logger.info("Attiva codice Immagine - Agosto")
        return """
<div align="center">
<p></p>
<center>
    <img border="0" src="../Fondo-streaming.jpg" width="640" height="400" valme_date="August" />	
</center></div>
"""
        
    else:
        logger.info("Attiva codice Immagine - No Luglio - No Agosto")
        return """
<div align="center">
<p></p>
<center>
    <img border="0" src="../Fondo-streaming.jpg" width="640" height="400"  valme_date="normal" />
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
	


