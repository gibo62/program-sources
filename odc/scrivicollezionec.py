import mysql.connector
from mysql.connector import Error
import os
import pathlib
import datetime
import time
import platform

tipo="M2V"


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
        print(f"Error: '{err}'")
        

def insert_row(campi):
    printdebug(campi)
    printdebug (str(len(campi))+" "+str(len(nometipo1)))
    sql="insert into media_DiscoC("
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
        sql=sql+"'"+campi[i]+"'"
    sql=sql+")"
    return sql


        
debug= False
conn = create_db_connection("localhost", "root", "NostraSignoradellaLuce2024","video_metadata")

filename="D:\\Users\\gilbe\\OneDrive\\Opera della chiesa\\conservazione\\catalogos\\INVENTARI\\DVD_VOB.txt"
nometipo1=["drive","campo1","campo2","campo3","titolo","campo5","NomeFile","data_modifica","data_accesso","data_creazione"]

a="d"
righe=0
record=0
w = os.walk("d:\\")
for (dirpath, dirnames, filenames) in w:
    for file in filenames:
        if file[-4:] == ".M2V" or file[-5:] == ".mpeg" or file[-4:] == ".M2T" or file[-5:] == ".M2TS" or file[-4:] ==".MTS":
            percorso=dirpath
            p=pathlib.Path(percorso)
            campi=percorso.split('\\')
            for elementi in range (len(campi), 6):
                campi.append("N/A")
            if campi[4] == "N/A":
                campi[4]=campi[3]
                campi[3]="N/A"
            campi.append (file)
            campi.append (str(datetime.datetime.fromtimestamp(p.stat().st_ctime)))
            campi.append (str(datetime.datetime.fromtimestamp(p.stat().st_atime)))
            campi.append (str(datetime.datetime.fromtimestamp(p.stat().st_mtime)))            
            sql=insert_row(campi)
            printdebug (sql)
            righe=righe+1
            if a=="d" and debug:
                a=input(campi)
            record=record+1
            execute_query(conn, sql)
            if a == "n":
                    break
conn.close()
print(righe, record)
    

