# To enable I2C, add the following to /boot/config.txt
#dtparam=i2c1=on
#dtparam=i2c0=on

import time
import numpy as np

import cv2
import picamera
import picamera.array
import os
from datetime import datetime

temp_val = 512
min_focus = 1002
max_focus = 2
close_focus = 430
# autofocus stuff    
max_index = 10
max_value = 0.0
last_value = 0.0
dec_count = 0
focal_distance = 10
auto_flag = False

mode = 0
resolution = ['2592x1944', '1920x1080', '1640x1232', '1280x720', '640x480']
resolution_idx = 4 # set to max so will cycle back when first called

frame_shape = None
fr = 15


def run():
    global auto_flag, mode, resolution, resolution_idx, fr
    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Frame", 640, 480)
    
    
    with picamera.PiCamera() as camera:
        # Set the camera resolution
        x = 400
        #camera.resolution = (int(1.33 * x), x)
        # Various optional camera settings below:
        # camera.framerate = 5
        # camera.awb_mode = 'off'
        # camera.awb_gains = (0.5, 0.5)
        camera.framerate = 27.5

        # Need to sleep to give the camera time to get set up properly
        time.sleep(1)
        temp_val = 512

        with picamera.array.PiRGBArray(camera) as stream:
            # Loop constantly
            while True:
                # Grab data from the camera, in colour format
                # NOTE: This comes in BGR rather than RGB, which is important
                # for later!
                camera.capture(stream, format='bgr', use_video_port=True)
                image = stream.array
                display(image)
                
                stream.truncate(0)

                # If we press ESC then break out of the loop
                k = cv2.waitKey(7) % 0x100
                action = chr(k)
                if k == 27:
                    break
                elif action == 'q':
                    break
                elif action == 'c':
                    print("Capture") 
                    title = '/home/pi/Pictures/' + format(datetime.now(), '%Y%m%d%H%M%S-') + str(x) + '.jpg'
                    camera.capture(title, quality=25)                
                elif action == 'd':
                    if camera.revision == 'ov5647':
                        print('Version 1', camera.revision)
                    elif camera.revision == 'imx219':
                        print('Version 2', camera.revision)
                    else:
                        print('Revision', camera.revision)        
                    print('Sensor Mode', camera.sensor_mode)
                    print('Rotation', camera.rotation)
                    print("Shutter speed:", camera.shutter_speed)
                    #print("Frame", camera.frame)
                    print("Frame Rate", camera.framerate)
                    print("Resolution", camera.resolution)
                    print("Image", frame_shape)
                elif action == 'f':
                    print("Flip", camera.hflip)
                    camera.hflip
                    print(camera.hflip)
                elif action == 'r':
                    if camera.rotation == 0:
                        camera.rotation = 180
                    else:
                        camera.rotation = 0
                    print("Rotation", camera.rotation)
                elif action == 'i':                    
                    if temp_val < 1000:
                        temp_val += 10
                    else:
                        temp_val = temp_val
                    print("Motor", temp_val)
                    set_focus(temp_val)
                elif action == 'o':
                    if temp_val <12 :
                        temp_val = temp_val
                    else:
                        temp_val -= 10
                    print("Motor", temp_val)                        
                    set_focus(temp_val)
                elif action == 'm':
                    set_focus(max_focus)
                elif action == 'n':
                    set_focus(min_focus)
                elif action == 'z':
                    set_focus(close_focus)
                elif action == 'x':  # change frame rate
                    fr = fr + 2.5
                    if fr > 30:
                        fr = 15
                    print("Frame rate:", fr)                        
                    camera.framerate = fr
                elif action == 'a':
                    max_index = 10
                    max_value = 0.0
                    last_value = 0.0
                    dec_count = 0
                    focal_distance = 10
                    auto_flag = True
                elif action == 'b':
                    resolution_idx += 1
                    if resolution_idx > 4:
                        resolution_idx = 0
                    camera.resolution = resolution[resolution_idx]
                    print("Resolution", camera.resolution)        
                                        
                
                

    # Important cleanup here!
    cv2.destroyAllWindows()
    width, height, depth = image.shape
    #print(image.shape)
    sz = out_width/height
    #print("Size", sz)
    im2 = cv2.resize(image, (int(height * sz), int(width * sz)))
    return im2

def set_focus(focus):
    value = (focus<<4) & 0x3ff0
    dat1 = (value>>8)&0x3f
    dat2 = value & 0xf0
    os.system("i2cset -y 0 0x0c %d %d" % (dat1,dat2))
    
def laplacian(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    img_sobel = cv2.Laplacian(img_gray,cv2.CV_16U)
    return cv2.mean(img_sobel)[0]
    
def auto_focus(image):
    global max_value, max_index, focal_distance, last_value, dec_count, auto_flag
    #initialize
    
    #print("Start focusing")
    val = laplacian(image)
    #print("Value", val)
    #Find the maximum image clarity
    if val > max_value:
        print("Increase")
        max_index = focal_distance
        max_value = val
            
    #If the image clarity starts to decrease
    if val < last_value:
        print("Decrease")
        dec_count += 1
    else:
        dec_count = 0
    #Image clarity is reduced by six consecutive frames
    print("Count", dec_count)
    if dec_count > 6:
        auto_flag = False
        return
    last_value = val
        
    #Increase the focal distance
    focal_distance += 10
    if focal_distance > 1000:
        auto_flag = False
        return

    #Adjust focus to the best
    print("Focus", max_index, "Value", val, max_value, last_value)
    set_focus(max_index)
    
def display(frame):
    global frame_shape
    # Display
    # Resize for display
    image = cv2.resize(frame, (640, 480))
    frame_shape = image.shape
    # Need to flip camera vertically
    im2 = cv2.flip(image, 0)
    if auto_flag:
        auto_focus(im2)
        
    cv2.imshow("Frame", im2)
    
    

if __name__ == '__main__':
    run()
