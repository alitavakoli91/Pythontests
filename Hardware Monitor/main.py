#!/usr/bin/python3
import cpu
import disks
import meminfo
import rx_monitor.py
import tx_monitor.py

printlist = [(cpu.top),(disks.lsblk),(meminfo.meminfo),(rx_monitor.rx),(tx_monitor.tx)]

print(printlist)


