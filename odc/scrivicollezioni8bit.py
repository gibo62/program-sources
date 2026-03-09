import mysql.connector
from mysql.connector import Error
from pymediainfo import MediaInfo
import os
import pathlib
import datetime
import time
import platform

tipo="M2V"


def convert_to_preferred_format(sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   minuti = sec // 60
   sec %= 60
   return "%02d:%02d:%02d" % (hour, minuti, sec) 

def printdebug(msg):
    if debug:
        print(msg)
        
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        printdebug("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        printdebug("Query successful")
    except Error as err:
        print (query)
        print(f"Error: '{err}'")
        a=input
        
        

def insert_row(campi):
    printdebug(campi)
    printdebug (str(len(campi))+" "+str(len(nometipo1)))
    sql='insert into media_8bit('
    if len(campi)> len (nometipo1):
        elementi=len(nometipo1)
    else:
        elementi=len(campi)
    for i in range(0,elementi):
        if i != 0:
            sql=sql+', '
        sql=sql+nometipo1[i]
    sql=sql+') values ('
    for i in range(0,elementi):
        if i != 0:
            sql=sql+', '
        sql=sql+'"'+campi[i]+'"'
    sql=sql+')'
    return sql


        
debug= False

conn = create_db_connection("localhost", "root", "NostraSignoradellaLuce2024","video_metadata")

nometipo1=["drive","tipo","Video","Collana","Versione","campo1","campo2","campo3","campo4","campo5","campo6","campo7","NomeFile","data_modifica","data_accesso","data_creazione","dimensione","durata"]

a="d"
righe=0
record=0
letti=0
w = os.walk("d:\\")
for (dirpath, dirnames, filenames) in w:
    for file in filenames:
        if file[-4:] != ".ele":
            percorso=dirpath
            p=pathlib.Path(percorso)
            file_intero=str(p)+"\\"+file
            dimensione_file=os.path.getsize(str(p)+"\\"+file)/1024
            clip_info = MediaInfo.parse(file_intero)
            duration_ms = clip_info.tracks[0].duration
            printdebug(duration_ms)
            if duration_ms is None:
                durata_video="N/A"
            else:
                durata_video=convert_to_preferred_format(int(duration_ms/1000))
            printdebug("durata Video: "+durata_video)
            campi=percorso.split('\\')
            if debug:
                print (len(campi))
                print(campi)
                a=input(file)
            for elementi in range (len(campi), 12):
                campi.append("N/A")
            campi.append (file)
            campi.append (str(datetime.datetime.fromtimestamp(p.stat().st_ctime)))
            campi.append (str(datetime.datetime.fromtimestamp(p.stat().st_atime)))
            campi.append (str(datetime.datetime.fromtimestamp(p.stat().st_mtime)))            
            campi.append (str(dimensione_file))
            campi.append (durata_video)
            sql=insert_row(campi)
            printdebug (sql)
            righe=righe+1
            if a=="d" and debug:
                a=input(campi)
            record=record+1
            execute_query(conn, sql)
            if a == "n":
                    break
        else:
            print (file)
        letti=letti+1
        print (letti,righe)
conn.close()
print(letti, righe, record)
    

