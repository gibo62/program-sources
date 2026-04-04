#!/usr/bin/python
import os
nomefile="/home/nsvalme/prova.txt"
file = open(nomefile, "w")
file.write("video\n")
file.close()

cmd = "pidof ffmpeg"
shellcmd = os.popen(cmd)
cmd="kill "+str(shellcmd.read())
print (cmd)
shellcmd = os.popen(cmd)
print(shellcmd.read())

