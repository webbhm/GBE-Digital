from rtc import RealTimeClock
from exp import exp
import Exp_Util
from Exp_Day import exp_day

def check_phase():
    rtc = RealTimeClock()
    if rtc._lost_power:
        print("Power", rtc._lost_power)
        print(rtc.get_datetime())
        # exit if don't have valid time
        return None
    #print("Good RTC")
    dy = exp_day()
    phase = 0
    for d in exp["phase_change"]:
        if dy >= d:
            # move to next phase
            phase += 1
    if phase > exp["current_phase"]:
        exp["current_phase"] = phase
        # save back
        Exp_Util.save(exp)
    return phase
            
def test():
    print("Check Phase")
    status = check_phase()
    print(status)
    if status is not None:
        print("Current Phase:", status)
    else:
        print("Bad Clock time")
if __name__ == "__main__":
    test()
            
    
    