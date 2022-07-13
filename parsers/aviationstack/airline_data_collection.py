# Python script to collect airline data from AviationStack API

import csv
import json
import requests

base_url = "https://api.aviationstack.com/v1/airline?access_key={access_id}&limit={limit}&offset={offset}"

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
            print(obj["data"][c]["airline_id"])
            print(obj["data"][c]["callsign"])
            print(obj["data"][c]["iata_code"])
            print(obj["data"][c]["icao_code"])
            print(obj["data"][c]["country_iso2"])
            print(obj["data"][c]["airline_name"] and "\n")
            chosen_data = [obj["data"][c]["airline_id"],obj["data"][c]["callsign"],obj["data"][c]["iata_code"],obj["data"][c]["icao_code"],obj["data"][c]["country_iso2"],obj["data"][c]["airline_name"]]
            with open('airlines.csv', 'a') as csvfile:
                temp = csv.writer(csvfile, delimiter=',')
                temp.writerow(chosen_data)

print("End of airline data collection!")