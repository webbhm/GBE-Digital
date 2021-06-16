import os

for x in range(1001):
    w = round(x/1000, 4)
    cmd = 'echo "12={} 16={} 20={} 21={}" > /dev/pi-blaster'.format(1, 1, 1, w)
    print(cmd)
    os.system(cmd)        
    

