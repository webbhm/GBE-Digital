'''
Utility to take a sensor record and log to a CSV file
Works for periodic appending of new data
Author: Howard Webb
Date: 12/14/2019

'''

import os, sys
from time import sleep
import csv

env_header = ['type', 'source', 'timestamp', 'subject', 'attribute', 'value', 'units', 'status', 'status_qualifier', 'comment']
file_name = "Data.csv"
DIR = "/home/pi/data/"

class CSV_Util(object):
    
    def __init__(self, file=file_name, header=env_header):
        self._file_name = DIR + file
        self._file = None
        print("File", self._file_name)
        try:
            os.stat(self._file_name)
        except:
            # If new append then need header
            self.save(header)
            print("Header written")

    def save(self, rec):
        with open(self._file_name, 'a+', newline='') as f:
            wr = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            wr.writerow(rec)
       


    def get_list(self):
       #print(self._file_name)
       with open(self._file_name, 'r') as f:
           rr = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
           doc = list(rr)
           return doc
       

      
    def check_thumb(self):
     
        try:
            os.listdir('D:/data')
            print("/sd Mounted")
        except:
            print("SD not found")

            return False
        print("SD Mounted")    
        return True        
       
    def get_file(self):
        print("In Get File")
        f = None
        try:
            #print("Found", os.listdir('/sd/data'))
            print("File", self._file_name)
            f = open(self._file_name, 'a')
#             print("Opened", self._file_name)
            return f
            
        except Exception as e:
            print("Failure opening file", self._file_name, e)
            self.check_sd()
            f = open(self._file_name, self._mode)
            return f
        return f
        
      
def test():
    env_header = ['type', 'source', 'timestamp', 'subject', 'attribute', 'value', 'units', 'status', 'status_qualifier', 'comment']
    rec = ['EnvObsv', '123', '2020-11-03T10:00:00', 'Water', 'Temp', 22, 'C', 'Complete', 'Success', '']
    file_name = "Data.csv"
    
    util = CSV_Util(file_name, env_header)
    print("Save:", file_name)
    util.save(rec)
    print("Done")

def test2():
    util = CSV_Util(file_name, env_header)
    util.get_list()
    
if __name__ == "__main__":
    test()
