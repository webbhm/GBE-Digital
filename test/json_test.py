# Test conversions between dictionary, text and back to dictionary
import json

data_set = [{"cmd":"LIGHT_ON"}, {"cmd":"LIGHT_OFF"}, {"cmd":"LIGHT_SET", "args":{"R":45,"G":68, "B":77, "W":83}}, {"cmd":"Foo"}]

for data in data_set:
    print("Dict", data)
    dmp = json.dumps(data)
    print("Str", dmp)
    bk = json.loads(dmp)
    print("Back", bk)
    print(bk["cmd"])
    

