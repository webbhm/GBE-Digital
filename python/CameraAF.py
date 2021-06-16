from picamera import PiCamera
from time import sleep
import datetime
import os
from PIL import Image

class Camera(object):
    
    def __init__(self):
        self._camera = PiCamera(resolution=(1024, 768))
        self._camera.rotation = 180
    # Set focus
    focus = 450 # 6 to 14 inches
    value = (focus<<4) & 0x3ff0
    dat1 = (value>>8)&0x3f
    dat2 = value & 0xf0
    print("Set Focus")
    try:
        ret = os.system("i2cset -y 0 0x0c %d %d" % (dat1,dat2))
        print("OS Err", ret)
    except Exception as e:
        print("Error", e)
    print("initialized")

    sleep(2)
    
    def __del__(self):
        self._camera.close()
    
    def capture(self, file_name = None):
        if file_name == None:
            file_name = '/home/pi/Pictures/' + format(datetime.datetime.now(), '%Y-%m-%d_%H%M') + '.jpg'
        print(file_name)
        self._camera.capture(file_name)
        
    def lapse(self):
        file_name = '/home/pi/Pictures/' + format(datetime.datetime.now(), '%Y-%m-%d_%H%M') + '.jpg'
        self.capture(file_name)
        im = Image.open(file_name)
        im2 = im.resize((240, 240))
        fl = file_name.split("/")
        #print(fl)
        new_name = '/{}/{}/{}/lapse/{}'.format(fl[1], fl[2], fl[3], fl[4])
        #print(new_name)
        print(new_name)
        im2.save(new_name)
        
def test():
    print("Camera Test")
    c = Camera()
    print("Capture")
    c.capture()
    print("Lapse")
    c.lapse()
    print("Done")
    
if __name__ == "__main__":
    test()
                        
