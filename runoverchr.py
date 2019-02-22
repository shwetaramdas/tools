#!/bin/python

import os
import sys

command = sys.argv[1]

for chr in range(1, 23):
        chrstr = str(chr)
        command2 = command.replace("XXX", chrstr)
        print(command2)
        os.system(command2)
