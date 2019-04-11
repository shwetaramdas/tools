#!/bin/python

import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--command","-c",type=str)
parser.add_argument("--parallel",action="store_true")

args = parser.parse_args()
command = args.command

for chr in range(1, 23):
	chrstr = str(chr)
	command2 = command.replace("XXX", chrstr)
	print(command2)
#	os.system(command2)

	if args.parallel:
		os.system(command2 + " &")
	else:
		os.system(command2)
