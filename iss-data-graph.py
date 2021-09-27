import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import json

file_path = 'iss-data.json'

latitude,longitude = [],[]

with open(file_path, 'r') as f:
    data = json.load(f) #current data has 169 items

for i in data:
    latitude.append(i["iss_position"]["latitude"])
    longitude.append(i["iss_position"]["longitude"])

plt.plot(latitude[:10], longitude[:10],'o-') #remove the index to plot all points
plt.title("ISS location")

plt.xlabel("Latitude")
plt.ylabel("Longitude")

plt.show()
