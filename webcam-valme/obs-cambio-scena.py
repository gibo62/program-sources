#!/usr/bin/python3
import cgi
import sys

from obswebsocket import obsws, requests

# Configurazione connessione OBS
host = "localhost"
port = 4455
password = "lfAFIRqJrhruEsvM" # Impostata in OBS

scene_name = "Image" # Il nome della scena da attivare
form = cgi.FieldStorage()
scene_name=form.getvalue('scena')
if len(sys.argv) == 2:
        nome_script, scene_name = sys.argv
# Connessione a OBS
ws = obsws(host, port, password)
ws.connect()

try:
    # Richiesta di cambio scena
    ws.call(requests.SetCurrentProgramScene(sceneName=scene_name))
    print(f"Scena cambiata con successo a: {scene_name}")
except Exception as e:
    print(f"Errore durante il cambio scena: {e}")
finally:
    # Disconnessione
    ws.disconnect()
