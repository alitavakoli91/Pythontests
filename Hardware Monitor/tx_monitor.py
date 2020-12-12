#!/usr/bin/python3

from time import sleep

def get_tx_bytes():
	while True:
		with open("/sys/class/net/wlp9s0/statistics/tx_bytes", "r") as f:
			tx_bytes = f.readline()
		yield tx_bytes
				
tx_bytes = get_tx_bytes()

while True:
	tx_current = int(next(tx_bytes))
	sleep(1)
	tx_afer_1sec = int(next(tx_bytes))
	tx = print(f"TX Speed - Mbps : {(tx_afer_1sec - tx_current) / 1024 / 1024 * 8 }" , end="\r")





