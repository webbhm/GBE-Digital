'''
Converts start-time to experiment day (number of days since launch)

Author: Howard Webb
Date: 3/2/2021
'''

import datetime
from exp import exp

def dif_dates(date1,date2):
    # calc days difference between dates
    return(abs(date2-date1).days)

def exp_day():
    # determine difference between start_date and current time
    dt1 = exp["start_date"]
    reply = None
    #print(dt1)
    if dt1 is None:
        return 0
        d1 = dt1
    out = dt1.split('-')
    #print(out[0], out[1], out[2][:2])
    # split into parts
    yr = int(out[0])
    m = int(out[1])
    d = int(out[2][:2])
    # convert to date object         
    d1 = datetime.date(yr, m, d)
    # get current date as object
    d2 = datetime.date.today()
    # clac difference
    day = dif_dates(d2, d1) + 1    
    #print("Day: {} Now: {} Start: {}".format(day, d2, d1))
    return day 
    
def test():
    day = exp_day()
    reply = 'Exp Day: {}'.format(day)
    print(reply)
    
if __name__ == "__main__":
    test()
    