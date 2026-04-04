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
<link href="http://retesrl.biz/livetest/livealbanosanpietro/js/video-js/video-js.min.css" rel="stylesheet">
<script src="http://retesrl.biz/livetest/livealbanosanpietro/js/video-js/ie8/videojs-ie8.min.js"></script>
<script src="http://retesrl.biz/livetest/livealbanosanpietro/js/video-js/video.min.js"></script>
<script src="http://retesrl.biz/livetest/livealbanosanpietro/js/video-js/videojs-contrib-hls.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>

<div style="max-width: 640px; margin: 0 auto; overflow:hidden;">
    
<!-- video stream inicio -->
<video id="video" class="video-js vjs-default-skin vjs-big-play-centered" controls autoplay preload="auto" data-setup='{"aspectRatio":"16:9" }' style="width:100%; height:auto;">
<!--<source src="https://erosvm3.indigitaleweb.com/live_albanosanpietro/albanosanpietro.stream/playlist.m3u8" type="application/x-mpegURL">-->
<p class="vjs-no-js">To view this video please enable JavaScript, and consider upgrading to a web browser that <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a></p>
</video>
<!-- video stream fin -->   

    
<script>
    /*
 NO SE VE!!!
<!-- video youtube inicio -->
<iframe style="width:100%; min-height:360px; height:auto;" src="https://www.youtube.com/embed/F5AcTA0LfVA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<!-- video youtube fin -->

*/
</script>
</div>
<script>    
    /*// Set the HLS overrideNative option globally
    videojs.options.hls.overrideNative = true;
    // Player instance options
    var options = {
        html5: {
            nativeAudioTracks: true,
            nativeVideoTracks: true
        }
    };
    var player = videojs('video', options);*/
          var video = document.getElementById('video');
      if(Hls.isSupported()) {
        var hls = new Hls();
        hls.loadSource('https://erosvm3.indigitaleweb.com/live_albanosanpietro/albanosanpietro.stream/playlist.m3u8');
        hls.attachMedia(video);
        hls.on(Hls.Events.MANIFEST_PARSED,function() {
          video.play();
      });
     }
     else if (video.canPlayType('application/vnd.apple.mpegurl')) {
        video.src = 'https://erosvm3.indigitaleweb.com/live_albanosanpietro/albanosanpietro.stream/playlist.m3u8';
        video.addEventListener('loadedmetadata',function() {
          video.play();
        });
      }
</script>
</div>
"""
    if comando=="attivaimmagine" and datetime.datetime.now().month == 7:
        logger.info("Attiva codice Immagine - Luglio")
        return """
<div align="center">
<p></p>
<center>
    <img border="0" src="../spietroapostolo2.jpg" width="640" height="400" valme_date="july" />
</center></div>
"""
    
    elif comando=="attivaimmagine" and datetime.datetime.now().month == 8:
        logger.info("Attiva codice Immagine - Agosto")
        return """
<div align="center">
<p></p>
<center>
    <img border="0" src="../spietroapostolo2.jpg" width="640" height="400" valme_date="august" />
</center></div>
"""
        
    else:
        logger.info("Attiva codice Immagine - No Luglio - No Agosto")
        return """
<div align="center">
<p></p>
<center>
    <img border="0" src="../spietroapostolo2.jpg" width="640" height="400"  valme_date="normal" />
</center></div>
"""



form = cgi.FieldStorage()
print "Content-type: text/html" 
print 
print "<HTML><HEAD></HEAD><BODY>" 
comando=form.getvalue('comando')
f = open('../disattiva_spa.txt')
content = f.read()
f.close
if "dis-off" in content:
    logger.info("Automatismo Abilitato")
    Html_file= open("../embed_homepage_spa.html","w")
    Html_file.write(attiva(comando))
    Html_file.close()
    logger.info("Pagina Embed_homepage_spa.html creata")
    print "</BODY></HTML>"
else:
    logger.info("Automatismo Disabilitato: Pagina Embed_homepage_spa.html non sovrascritta")


