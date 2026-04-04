FUNZIONAMENTO DELLE CAM per le parrocchie di:
- Nostra Signora di Valme (Roma)
- San Pietro Apostolo (Albano)


STEP 1)  index.html: contiene il codice per scegliere se attivare la CAM

STEP 2) attivacam.py (chiamato da index.html) gestisce il form per 
        scegliere se attivare oppure no la CAM

STEP 3) gestionecam.py (chiamato da attivacam.py o da script su webcam) contiene il codice che 
        controlla in che mese siamo e SCRIVE il file embed_homepage.html
        (inoltre scrive un file disattiva.txt)

STEP 4) embed_homepage.html è una normale pagina web che conterrà di volta in volta
        o lo script della webcam oppure un'immagine di sfondo


NOTA: sul sito web delle parrocchie è presente un banalissimo codice IFRAME 
      per embeddare embed_homepage.html in un blocco del sito