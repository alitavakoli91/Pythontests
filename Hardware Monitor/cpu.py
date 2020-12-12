#!/usr/bin/python3
from time import sleep
import os
while True:
	cls = os.system("clear")
	top = os.system("cat /proc/cpuinfo  | grep -i MHZ")
	sleep(1)
	
print(top)
