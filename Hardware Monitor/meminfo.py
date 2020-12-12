#!/usr/bin/python3
from time import sleep
import os
while True:
	cls = os.system("clear")
	meminfo = os.system("free -m")
	sleep(0.5)
print("Memory Usage : " , meminfo)
