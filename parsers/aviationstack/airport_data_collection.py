# Python script to collect airport data from AviationStack API

import csv
import json
import requests

base_url = "https://api.aviationstack.com/v1/airport?access_key={access_id}&limit={limit}&offset={offset}"

for i in range(10):
    current_url = base_url.format(access_id="ddc83050b33d14931df578e277fb192d", limit="1000", offset="0")
    r = requests.get(current_url, allow_redirects=True)
    obj = json.loads(r.content)
    total = (obj["pagination"]["total"])/1000
    total = int(total)

    for n in range(total):
        temp_url = base_url.format(access_id="ddc83050b33d14931df578e277fb192d", limit="1000", offset=n*1000)
        r = requests.get(temp_url, allow_redirects=True)
        obj = json.loads(r.content)
        
        for c in range(1000): # loop for 1000 values (the number of values in each api request)
            print(obj["data"][c]["airport_id"])
            print(obj["data"][c]["latitude"])
            print(obj["data"][c]["longitude"])
            print(obj["data"][c]["iata_code"])
            print(obj["data"][c]["icao_code"])
            print(obj["data"][c]["country_iso2"])
            print(obj["data"][c]["airport_name"] and "\n")
            chosen_data = [obj["data"][c]["airport_id"],obj["data"][c]["latitude"],obj["data"][c]["longitude"],obj["data"][c]["iata_code"],obj["data"][c]["icao_code"],obj["data"][c]["country_iso2"],obj["data"][c]["airport_name"]]
            with open('airports.csv', 'a') as csvfile:
                temp = csv.writer(csvfile, delimiter=',')
                temp.writerow(chosen_data)

print("End of airport data collection!")