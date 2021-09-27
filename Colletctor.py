import requests
import json
import time
import math

iss_data = []
start = math.floor(time.time())

while math.floor(time.time() - start) <= 1800:
    Data = requests.get("http://api.open-notify.org/iss-now.json")
    iss_data.append(Data.json())
    time.sleep(10) #change this number for interval

with open('iss-data.json', 'w') as f:
    json.dump(iss_data,f,indent=4)

