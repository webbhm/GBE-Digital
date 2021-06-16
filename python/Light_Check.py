import os
from exp import exp
from datetime import datetime

class CheckLight(object):
    # check if lights should be on or off
    def __init__(self):
        from exp import exp
        state = self.checkLight()
        print(state)

    def checkLight(self):
        """Check if lights should be on or off
        Args:
            test: flag for testing system
        Returns:
            None
        Raises:
            None
        """
        start_time = exp["phases"][exp['current_phase']]["lights"]["on"]["time"]
        end_time = exp["phases"][exp['current_phase']]["lights"]["off"]["time"]
        #print(start_time, end_time)
        
        state = self.determineState(start_time, end_time)
        if state:
            os.system('python3 /home/pi/python/Light_Switch.py -a on')
            return "On"
        else:
            os.system('python3 /home/pi/python/Light_Switch.py -a off')
            return "Off"
            
    def determineState(self, start, end):
        ''' Determine if lights should be on or off'''
        s=start.split(':')
        e=end.split(':')
        #print(s, e)
        # Munge date into times
        t=datetime.now()
        st=t.replace(hour=int(s[0]), minute=int(s[1]))
        et=t.replace(hour=int(e[0]), minute=int(e[1]))
        print("Start", st)
        print("End", et)
        print("Now", datetime.now())
        #print("After Start", st < datetime.now())
        #print("Before End", et > datetime.now())

        if st > et:
            # Night Light - roll to next day when lights go off
            print("Span Day")
            et += timedelta(days=1)

        msg = "{} {} {} {}".format("Start Time: ", st, "End Time: ", et)
        
        if (st < datetime.now()) and (et > datetime.now()):
            msg="Lights should be On"
            return True
        else:
            msg="Lights should be Off"
            return False
        return
    
def test():
    print("Test CheckLight")
    cl = CheckLight()
    
if __name__ == "__main__":
    test()