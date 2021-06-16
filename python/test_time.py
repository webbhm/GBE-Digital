def confirm(values):
    print("Set Time", values)
    from datetime import datetime
    from rtc import RealTimeClock
    hour = values[0]
    minute = values[1]

    #print("Time", hour, minute)

    # set the time based on input
    # get current if date already set
    dt = datetime.now()
    t = dt.timetuple()

    try:
    # 
        from rtc import RealTimeClock
        rtc = RealTimeClock()
        # get current values - keep date
        t = rtc.get_datetime()
        #print(t)
        year = t.tm_year
        month = t.tm_mon
        day = t.tm_mday
        # set new time
        rtc.set_clock(year, month, day, hour, minute)
        # update raspberry
        rtc.set_raspberry()
    except Exception as e:
        print("Error:", e)
 

confirm([14, 31])
