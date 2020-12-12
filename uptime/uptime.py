#!/usr/bin/python3
import os

os.system("uptime -p >> uptime.txt")

f = open("uptime.txt", "r")
content = f.read()
print(content)
uptime = content.split(", ")
f.close()

f = open("uptime.txt", "w")
f.writelines("")
f.close()

x = uptime[1].split(" ")
num = int(x[0])

if num > 10:
	print("System was not restart")
else:
	print("System was restart")
