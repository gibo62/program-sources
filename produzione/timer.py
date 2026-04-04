#!/usr/bin/python
import time
import threading

# Variabile globale per ricordare l'ultima richiesta
ultimo_timestamp = 0
lock = threading.Lock()

def timer_reinizializzabile(durata):
    global ultimo_timestamp

    with lock:
        # Ogni chiamata aggiorna il "timestamp" e reinizializza il timer
        ultimo_timestamp = time.time()
        my_timestamp = ultimo_timestamp

    # Ciclo del timer
    while True:
        time.sleep(1)
        elapsed = time.time() - my_timestamp
        remaining = durata - elapsed

        # Se un'altra istanza ha resettato il timer -> interrompe questo timer
        if my_timestamp != ultimo_timestamp:
            return  # timer invalidato, esce

        if remaining <= 0:
            print("Timer scaduto!")
            return

        print(f"Tempo rimanente: {remaining:.1f} s", end="\r")


# Esempio d'uso
if __name__ == "__main__":
    # Simulazione: richiami il timer due volte
    threading.Thread(target=timer_reinizializzabile, args=(15,)).start()

    time.sleep(2)  # aspetti 2 secondi…

    # Richiamo del timer: reinizializza e riparte da zero
    threading.Thread(target=timer_reinizializzabile, args=(15,)).start()
