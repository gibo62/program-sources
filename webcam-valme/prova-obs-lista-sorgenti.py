#!/usr/bin/python3


import sys
from obswebsocket import obsws, requests

# Connessione al server WebSocket di OBS


# --- CONFIGURAZIONE ---
host = "localhost"
port = 4455  # Porta di default per OBS WebSocket 5
password = "lfAFIRqJrhruEsvM" # Impostata in OBS
# ----------------------
ws = obsws(host, port, password)


def list_obs_sources():
    # Inizializza il client
    
    try:
        # Connetti a OBS
        ws.connect()
        print("Connesso a OBS Studio!<br>")
        
        # 1. Ottieni la lista delle scene
        scenes_data = ws.call(requests.GetSceneList())
        scenes = scenes_data.getScenes()
        
        print(f"\n--- Trovate {len(scenes)} Scene ---\n<br>")
        
        for scene in scenes:
            scene_name = scene['sceneName']
            print(f"\n[Scene]: {scene_name}<br>\n")
            
            # 2. Ottieni gli elementi (origini) per ogni scena
            items_data = ws.call(requests.GetSceneItemList(sceneName=scene_name))
            items = items_data.getSceneItems()
            
            if not items:
                print("  (Nessuna origine)<br>\n")
                continue
                
            for item in items:
                # Recupera nome e tipo dell'origine
                source_name = item['sourceName']
                source_type = item['inputKind'] if 'inputKind' in item else "Gruppo/Special"
                print(f"  - {source_name} ({source_type})\n<br>")
                
    except Exception as e:
        print(f"Errore: {e}<br>")
    finally:
        # Disconnetti
        ws.disconnect()
        print("\nDisconnesso.<br>")

if __name__ == "__main__":
    print ("Content-type: text/html\n\n")
    print
    print ("<HTML><HEAD></HEAD><BODY>")

#    list_obs_sources()
    reponse = ws.call(requests.GetCurrentProgramScene())
    print (response)

    print ("</BODY></HTML>")


