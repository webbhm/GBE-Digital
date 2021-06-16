import os

pin_R = 12 # Red
pin_B = 20 # Blue
pin_G = 16 # Green
pin_W = 21  # White

OFF = 1

#      echo "17=0.2" > /dev/pi-blaster
r = 1
g = 1
b = 1
w = 0

cmd = 'echo "12={} 16={} 20={} 21={}" > /dev/pi-blaster'.format(r, g, b, w)
print(cmd)
os.system(cmd)