#!/usr/bin/python3
 
import psutil
import os
from signal import SIGKILL

process_name = "ffmpeg"
pid = None

for proc in psutil.process_iter():
    if process_name in proc.name():
       pid = proc.pid
       break

print("Pid:", pid)
os.kill(pid, SIGKILL)
