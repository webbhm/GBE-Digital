import argparse

parser = argparse.ArgumentParser(description='Control the Grow Light.')
parser.add_argument("--a", help="Turn the light on or off", type=str, choices=["On", "Off", "on", "off"])
args = parser.parse_args()
if args.a in ["On", "on"]:
    print("Light turned On")
if args.a in ["Off", "off"]:
    print("Light turned Off")