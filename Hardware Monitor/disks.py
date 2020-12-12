#!/usr/bin/python3
from time import sleep
import os
while True:
	cls = os.system("clear")
	lsblk = os.system("lsblk | grep sd")
	sleep(1)
	
print(lsblk)
