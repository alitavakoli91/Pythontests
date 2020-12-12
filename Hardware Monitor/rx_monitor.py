#!/usr/bin/python3

from time import sleep
def get_rx_bytes():
	while True:
		with open("/sys/class/net/wlp9s0/statistics/rx_bytes", "r") as f:
			rx_bytes = f.readline()
		yield rx_bytes
				
rx_bytes = get_rx_bytes()

while True:
	rx_current = int(next(rx_bytes))
	sleep(1)
	rx_afer_1sec = int(next(rx_bytes))
	rx = print(f"RX Speed - Mbps : {(rx_afer_1sec - rx_current) / 1024 / 1024 * 8 }" , end="\r")
