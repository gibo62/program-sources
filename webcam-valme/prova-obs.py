#!/usr/bin/python3

from obswebsocket import obsws, requests

# Connessione al server WebSocket di OBS
host = "localhost"
port = 4455
password = "lfAFIRqJrhruEsvM" # Impostata in OBS

ws = obsws(host, port, password)
ws.connect()

# Avvia lo streaming
ws.call(requests.StartStream())

# Chiudi la connessione
ws.disconnect()
