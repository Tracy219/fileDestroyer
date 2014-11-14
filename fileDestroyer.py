#!/usr/bin/env python
# This program is really dangerous!!! It can destroy a file!!!!!

from specialInput import *
import os

fileName = raw_input("What file should I destroy? ")
if not os.path.isfile(fileName):
	print("I don't think that\'s a file exist in this computer.")
	exit()

times = int_input("How many times should I overwrite it? ")

answer = raw_input("WARNING: This will destroy all data in {} \n" \
"Are you sure you want to continue? ".format(fileName))

if answer[0].lower() == 'y':
	f = open(fileName, "r+")
	numbers = f.read()

	for i in range(times):
		f.seek(0)
		f.write(chr(i + 65) * len(numbers))
		print("Pass {}: Writing file with all {}'s".format(i + 1, chr(i + 65)))

	f.close()
	os.system("rm {}".format(fileName))
	print("{} has been securelt deleted.".format(fileName))

else:
	print("May I ask you why you open this program, just for fun?")