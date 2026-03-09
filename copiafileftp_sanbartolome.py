import os
import ftplib
from urllib.parse import unquote
import re
import datetime

def write_log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.write(f"[{timestamp}] {message}\n")
    
drivepath='g:\\il mio drive\\sanbartolome\\'
log= open(drivepath+"ftptrasfer.log", "a")  # append mode
write_log("Attività iniziata")

with ftplib.FTP("sbartolome.nsvalme.cloud", "sanbartolome", "Siviglia!2026") as ftp:
    ftp.cwd('/home/sanbartolome')
    filenames = ftp.nlst()
    print (filenames)

    for filename in filenames:
        decoded = unquote(filename)
        # Regex per estrarre data e ora
        pattern = r"record_(\d{4}-\d{2}-\d{2})_(\d{2}:\d{2}:\d{2})\.mkv"
        match = re.match(pattern, decoded)
        if match:
            data = match.group(1)
#           ora = match.group(2)
#            print("Data:", data)
#            print("Ora:", ora)
#            print("Formato non riconosciuto")
            anno, mese, giorno = data.split("-")
#            print("Anno:", anno)
#            print("Mese:", mese)
#            print("Giorno:", giorno)
            directory = drivepath+anno
            os.makedirs(directory, exist_ok=True)
            directory = drivepath+anno+"\\"+mese
            os.makedirs(directory, exist_ok=True)   
            nomefile=drivepath+anno+"\\"+mese+"\\"+filename.replace(":","-")
            if os.path.isfile(nomefile):
                write_log("il file: "+nomefile+" esiste; non viene copiato!")
                print("Il file esiste!")
            else:
                print("Il file non esiste!")
                print (filename,nomefile)
                with open(nomefile, 'wb' ) as file :
                    ftp.retrbinary('RETR %s' % filename, file.write)
                    write_log("il file: "+nomefile+" non esiste; copiato da "+filename)
                    file.close()
            write_log("il file: "+filename+" viene cancellato!")
            ftp.delete(filename)
        else:
            write_log("formato non riconosciuto "+decoded)         
    ftp.quit()
    
log.close()
