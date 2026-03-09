import mysql.connector

connection_metadata = mysql.connector.connect(host='localhost', user='root', password='NostraSignoradellaLuce2024', database='video_metadata')
cursor_metadata = connection_metadata.cursor()
connection_bd = mysql.connector.connect(host='localhost', user='root', password='NostraSignoradellaLuce2024', database='videosbd')
cursor_bd = connection_bd.cursor()

def fetch_firma():
    query = "SELECT Firma FROM tablamediainfo_8bit"
    cursor_metadata.execute(query)
    positions = cursor_metadata.fetchall()
    print("Posizioni disponibili:")
    for position in positions:
        firma=position[0].replace("-","")
        print(firma)
        query = "SELECT CodVersion FROM versiones where ManifiestoBagit like '%"+firma+"%'"
#        input (query)
        cursor_bd.execute(query)
        righe = cursor_bd.fetchall()
#        print (cursor_bd.rowcount)
        if cursor_bd.rowcount > 0:
#            print (righe)
            for elementi in righe:
                inserimento="UPDATE tablamediainfo_8bit SET CodVersion = '"+elementi[0]+"' WHERE Firma = '"+position[0]+"'"
                cursor_metadata.execute(inserimento)
                connection_metadata.commit()
                print(cursor_metadata.rowcount, "record(s) affected") 
 #               print (inserimento)
    cursor_bd.close()
    cursor_metadata.close()
    connection_metadata.close()
    connection_bd.close()
    
fetch_firma()

