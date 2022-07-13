# Python script for extracting list of station names from the Coop Station file provided by NOAA.
# The extracted station_list.txt will be used to pull weather data from NOAA API

import re

file = open("coop-stations.txt", "r")
text = file.read()
file.close()

matches = re.findall(" US(.+?) ", text) # extract station codes prefix US
mystring = "US"
matches = [mystring + s for s in matches]

newFile = open("station_list.txt", "w")
for element in matches:
    newFile.write(element + "\n")
newFile.close()