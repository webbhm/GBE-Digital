default_display = {
    "Def Dashboard":{"title":"Dashboard", "module":"Display_Dashboard", "class":"Dashboard", "config":"_column_list"},
    "Def Lapse":{"title":"Time Lapse", "module":"Display_Time_Lapse", "class":"TimeLapse", "config":"_column_list"},
    "Def Logo":{"title":"Logo", "module":"Display_Logo", "class":"DisplayLogo", "config":"_column_list"}
    }

def test():
    print("Default Display")
    print(default_display)
    
if __name__ == "__main__":
    test()    