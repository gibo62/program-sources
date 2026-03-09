import mysql.connector
from mysql.connector import Error

tipo="MPG9V"


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
    if not campi[2][len(campi[2])-1].isdigit():
        campi[2]="00000"+campi[2]
        campi[2]=campi[2][-5:]
    else:    
        campi[2]="0000"+campi[2]
        campi[2]=campi[2][-4:]
    sql="insert into media("
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
conn = create_db_connection("localhost", "root", "G!lberto1962","video_metadata")

filename="D:\\Users\\gilbe\\OneDrive\\Opera della chiesa\\conservazione\\catalogos\\INVENTARI\\DVD_VOB.txt"
nometipo1=["Drive","Tipo","Num_Video","Collezione","Versione","campo1","Dir1","NOMEFILE"]

a="d"
righe=0
record=0
with open(filename,'r',errors="ignore") as i_file:
    eof=False
    while not eof:
        line = i_file.readline().replace("'"," ")
        righe=righe+1
        if line:
            line = line.strip("\n")
            line = line.strip("\t")
            campi=line.split('\\')
            campi.insert (1,tipo)
            campi.pop(2)
            
            
            printdebug(campi)
            if len(campi) == 10:
                campi[5]=campi[7]
                campi.pop(7)
            if len(campi) > 8 and campi[6] == "MEDIA" and ("VTS_01_1.VOB" in campi[8]):
                campi.pop(7)
#               print (len(campi))
                if a=="d":
                    a=input(campi)
                sql=insert_row(campi)
                record=record+1
                printdebug (sql)
                execute_query(conn, sql)
                if a == "n":
                    break
        else:
            eof = True
    conn.close()
    i_file.close()
    print(righe, record)
    

