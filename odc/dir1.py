import os
import pathlib
import datetime
import time
import platform

w = os.walk("d:\\")
for (dirpath, dirnames, filenames) in w:
    for file in filenames:
        print (file)
#        a=input()
        if file[-4:] == ".M2V":
            percorso=dirpath+"\\"+file
            p=pathlib.Path(percorso)
            print (datetime.datetime.fromtimestamp(p.stat().st_ctime))
            print (datetime.datetime.fromtimestamp(p.stat().st_atime))
            dt = datetime.datetime.fromtimestamp(p.stat().st_mtime)
            campi=percorso.split('\\')
            print (campi)
            a=input (dt)
            if a == "e":
                exit()
                
