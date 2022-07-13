# Python script to collect flight data from AviationStack API

import csv
import json
import requests

with open('flight_dates.txt') as f:
    flight_dates = list(f.read().split("\n"))

with open('airport_icao.txt') as file:
    icao_codes = list(file.read().split("\n"))

base_url = "https://api.aviationstack.com/v1/flights?access_key={access_id}&flight_date={date}&limit={limit}&offset={offset}"

for i in flight_dates:
    current_url = base_url.format(access_id="ddc83050b33d14931df578e277fb192d", date=i.replace('\n',''), limit="1000", offset="0")
    open('historic_flight_urls.txt', 'a').write(current_url + "\n")
    r = requests.get(current_url, allow_redirects=True)
    obj = json.loads(r.content)
    total = (obj["pagination"]["total"])/1000
    total = int(total)

    for n in range(total):
        temp_url = base_url.format(access_id="ddc83050b33d14931df578e277fb192d", date=i.replace('\n',''), limit="1000", offset=n*1000)
        open('historic_flight_urls.txt', 'a').write(temp_url + "\n")
        r = requests.get(temp_url, allow_redirects=True)
        obj = json.loads(r.content)
        
        for c in range(1000): # loop for 1000 values (the number of values in each api request) checking each arrival and departure ICAO to be in icao_codes
            if (obj["data"][c]["departure"]["icao"] in icao_codes) and (obj["data"][c]["arrival"]["icao"] in icao_codes):
                print(obj["data"][c]["flight_date"])
                print(obj["data"][c]["departure"]["airport"])
                print(obj["data"][c]["departure"]["icao"])
                print(obj["data"][c]["departure"]["iata"])
                print(obj["data"][c]["departure"]["actual"])
                print(obj["data"][c]["arrival"]["airport"])
                print(obj["data"][c]["arrival"]["icao"])
                print(obj["data"][c]["arrival"]["iata"])
                print(obj["data"][c]["airline"]["name"])
                print(obj["data"][c]["airline"]["icao"])
                print(obj["data"][c]["flight"]["number"])
                print(obj["data"][c]["flight"]["iata"])
                print(obj["data"][c]["flight"]["icao"] and "\n")
                chosen_data = [obj["data"][c]["flight_date"],obj["data"][c]["departure"]["airport"],obj["data"][c]["departure"]["icao"],obj["data"][c]["departure"]["iata"],obj["data"][c]["departure"]["actual"],obj["data"][c]["arrival"]["airport"],obj["data"][c]["arrival"]["icao"],obj["data"][c]["arrival"]["iata"],obj["data"][c]["airline"]["name"],obj["data"][c]["airline"]["icao"],obj["data"][c]["flight"]["number"],obj["data"][c]["flight"]["iata"],obj["data"][c]["flight"]["icao"]]
                with open('flights2.csv', 'a') as csvfile:
                    temp = csv.writer(csvfile, delimiter=',')
                    temp.writerow(chosen_data)

print("End of script!")