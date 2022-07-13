# Script for collecting the daily summaries weather data from the NOAA Web Services API

import requests

base_url = "https://www.ncei.noaa.gov/access/services/data/v1?dataset={dataset}&dataTypes=AWND,PRCP,SNWD,SNOW,WSF2,TAVG,TMAX,TMIN&stations={station}&startDate={startDate}&endDate={endDate}&boundingBox=90,-180,-90,180&includeStationName=true&includeStationLocation=1&units=metric"

with open("station_list.txt", "r") as stations_file:
    for line in stations_file:
        current_url = base_url.format(dataset="daily-summaries", station=line, startDate="2021-12-01", endDate="2022-02-01") # specify parameters for date range, dataset type
        text_file = open("historic_urls.txt", "a") # write url to txt file for record keeping of previously collected data
        text_file.write("\n" + current_url)
        text_file.close()
        r = requests.get(current_url, allow_redirects=True)
        open('daily-summaries.csv', 'ab').write(r.content) # write CSV content to end of dataset file

print("End of weather data collection!")