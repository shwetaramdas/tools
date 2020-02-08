import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--command","-c",type=str,required=True)
parser.add_argument("--parallel",action="store_true")
parser.add_argument("--chr_start")
parser.add_argument("--chr_end")

args = parser.parse_args()
command = args.command

chr_start = 1
chr_end = 23

if args.chr_start:
        try:
                int(chr_start)
        except ValueError:
                print("chr_start must be in the range 1-22")
        chr_start = int(args.chr_start)

if args.chr_end:
        try:
                int(args.chr_end)
        except ValueError:
                print("chr_end must be in the range 1-22")
        chr_end = int(args.chr_end) + 1

if chr_start >= chr_end:
        raise ValueError('chr_end must be larger than chr_start')

for chr in range(chr_start, chr_end):
        chrstr = str(chr)
        command2 = command.replace("XXX", chrstr)
        print(command2)
#       os.system(command2)

        if args.parallel:
                os.system(command2 + " &")
        else:
                os.system(command2)
