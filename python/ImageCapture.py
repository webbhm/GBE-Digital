'''
Image Capture
1) Set camera lights
2) Take image
3) Save full image to Camer
4) Save small image to Camera/lapse
5) Reset lights

Author: Howard Webb
Date: 3/14/2021
3/16/2021 change to direct call of GrowLight
'''

from Light_Check import CheckLight
from time import sleep
from CameraAF import Camera
from GrowLight import GrowLight

gl = GrowLight()
print("Set Camera Light")
gl.camera()

print("Click")
sleep(5)
# Take Image
try:
    c = Camera()
    c.lapse()
except Exception as e:
    print("Camera failure: ", e)
# Reset light
CheckLight()