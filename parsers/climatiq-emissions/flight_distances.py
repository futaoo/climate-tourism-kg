# Python script to retrieve calculate the euclidean distances between two airports for CO2 Emission estimations

import requests, csv, json
import pandas as pd

base_url = "https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"

with open("unique_flights_sample.csv", "a") as file:
    reader = csv.reader(file, delimiter=",")
    df = pd.read_csv('unique_flights_sample.csv')
    df = df.reset_index()
    for index, row in df.iterrows():
        departure = row[4] + "%Airport"
        arrival = row[8] + "%Airport"
        current_url = base_url.format(address=departure, API_KEY="AIzaSyBPAI58u9Wfc7DZyTHL2JNnA7X8atu1ryU")
        r = requests.get(current_url, allow_redirects=True)
        obj = json.loads(r.content)
        df.at[index, 'lat1'] = obj["results"][0]["geometry"]["location"]["lat"]
        df.at[index, 'long1'] = obj["results"][0]["geometry"]["location"]["lng"]

        current_url = base_url.format(address=arrival, API_KEY="AIzaSyBPAI58u9Wfc7DZyTHL2JNnA7X8atu1ryU")
        r = requests.get(current_url, allow_redirects=True)
        obj = json.loads(r.content)
        df.at[index, 'lat2'] = obj["results"][0]["geometry"]["location"]["lat"]
        df.at[index, 'long2'] = obj["results"][0]["geometry"]["location"]["lng"]
        df.to_csv('out.csv', index=False, sep=',')
