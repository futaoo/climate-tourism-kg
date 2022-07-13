# program to take lat and long values of weather station and convert it to a tangible city name using the Google Maps API

import requests, csv, json, time
import pandas as pd

base_url = "https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"

with open("unique-airports.csv", "a") as file:
    reader = csv.reader(file, delimiter=",")
    df = pd.read_csv('unique-airports.csv')
    df = df.reset_index()
    for index, row in df.iterrows():
        temp = row[4] + "%Airport"
        current_url = base_url.format(address=temp, API_KEY="AIzaSyBPAI58u9Wfc7DZyTHL2JNnA7X8atu1ryU")
        r = requests.get(current_url, allow_redirects=True)
        obj = json.loads(r.content)
        df.at[index, 'latitude2'] = obj["results"][0]["geometry"]["location"]["lat"]
        df.at[index, 'longitude2'] = obj["results"][0]["geometry"]["location"]["lng"]
        df.to_csv('out.csv', index=False, sep=',')
