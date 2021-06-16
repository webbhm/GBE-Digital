'''
Simple file utility to move files to thumb drive
Does not assume knowledge of thumb drive name

Author: Howard Webb
Date: 2/26/2021
'''

import os
import glob

def remove(target):
    # delete target directory
    cmd = 'sudo rm -r {}'.format(target)
    os.system(cmd)

def copy(source, target):
    cmd = 'sudo cp -TR {} {}'.format(source, target)
    os.system(cmd)
    
def get_drive():
    # get name of thumb drive
    f = glob.glob("/media/pi/*/")
    if len(f) == 0:
        print("No Thumb Drive")
        return None
    print(f[0])
    return f[0]

def test():
    drive = get_drive()
    if drive is None:
        print("No drive found")
        exit(0)
    print(drive)
    home_dir = "/home/pi/"
    data_dir = "data"
    picture_dir = "Pictures"
    
    # move data
    print("Move Data")
    source = home_dir + data_dir
    target = drive + data_dir
    copy(source, target)    
    print("Moved", source, target)
    
    print("Move Pictures")
    source = home_dir + picture_dir
    target = drive + picture_dir
    copy(source, target)
    print("Moved", source, target)
    
    print("Move exp.py")
    file_name = "exp.py"
    source = home_dir + "python/" + file_name
    target = drive + file_name
    copy(source, target)
    print("Moved", source, target)

if __name__ == "__main__":
    test()
