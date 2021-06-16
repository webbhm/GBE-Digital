'''
Program to be called from cron for working with lights - on and off
This is a wrapper for the Client, handling command line parameters
Author: Howard Webb
Date: 2/10/2021
'''

import argparse
from exp import exp
from GrowLight import GrowLight

parser = argparse.ArgumentParser()
# list of acceptable arguments
parser.add_argument("-a", help="Send a light command (on, off, ...", type=str)
args = parser.parse_args()
#print(args)
gl = GrowLight()
if args.a == "on":
    gl.on()
elif args.a == "off":
    gl.off()
