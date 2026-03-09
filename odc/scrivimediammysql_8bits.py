import mysql.connector
from mysql.connector import Error
import os
import pathlib
import datetime
import time
import platform
import win32api

tipo="AVI"
ndisco=win32api.GetVolumeInformation("D:\\")[0]+"/7"

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
        return True
    except Error as err:
        print(f"Error: '{err}'")
        return False

def insert_row(campi):
    if not campi[2][len(campi[2])-1].isdigit():
        campi[2]="00000"+campi[2]
        campi[2]=campi[2][-5:]
    else:    
        campi[2]="0000"+campi[2]
        campi[2]=campi[2][-4:]
    campi.insert(0,campi[2]+campi[4])
    campi[7]=ndisco
    sql="insert into media_8bits("
    if len(campi)> len (nometipo1):
        elementi=len(nometipo1)
    else:
        elementi=len(campi)
    for i in range(0,elementi):
        if i != 0:
            sql=sql+", "
        sql=sql+nometipo1[i]
    sql=sql+") values ("
    for i in range(0,elementi):
        if i != 0:
            sql=sql+", "
        sql=sql+'"'+campi[i]+'"'
    sql=sql+")"
    return sql


        
debug= False
conn = create_db_connection("localhost", "root", "","video_metadata")

filename="D:\\Users\\gilbe\\OneDrive\\Opera della chiesa\\conservazione\\catalogos\\INVENTARI\\DVD_VOB.txt"
nometipo1=["keyvideocoll","drive","tipo","num_video","campo1","collezione","versione","num_disco","dir1","nomefile","data_modifica","data_accesso","data_creazione"]

a="d"
righe=0
record=0
w = os.walk("d:\\")
for (dirpath, dirnames, filenames) in w:
    for file in filenames:
        if file[-4:].upper() == ".AVI" or file[-4:].upper() == ".MKV":
            percorso=dirpath+"\\"+file
            p=pathlib.Path(percorso)
            campi=percorso.split('\\')
            campi.append (str(datetime.datetime.fromtimestamp(p.stat().st_ctime)))
            campi.append (str(datetime.datetime.fromtimestamp(p.stat().st_atime)))
            campi.append (str(datetime.datetime.fromtimestamp(p.stat().st_mtime)))
            sql=insert_row(campi)
            printdebug (sql)
            righe=righe+1
            if a=="d":
                a=input(campi)
            if execute_query(conn, sql):
                record=record+1
                
            if a == "n":
                    break
conn.close()
print(righe, record)
    

