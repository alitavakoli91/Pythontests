#!/usr/bin/python3
import os
appName = input("Enter your package name :")
x = os.system("apt list --installed | grep -i" + " " + appName)


print("Package was not Found ! \n")
