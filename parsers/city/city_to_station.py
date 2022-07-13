# script to connect a weather station to a nearby city based on X, Y co-ordinates

from scipy import spatial
import pandas as pd
import csv

city_df = pd.read_csv("uscities-large.csv", usecols=["latitude", "longitude"])
city_records = city_df.to_records(index=False)
cities = city_records.tolist()

tree = spatial.KDTree(cities)
out_df = pd.read_csv("uscities-large.csv", usecols=["city", "state_id", "latitude", "longitude", "population"])

with open('unique-stations.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        station_ref = row[0]
        lat = float(row[2])
        lng = float(row[3])
        result = tree.query([(lat,lng)], k=1, p=2.0)
        distance = float(result[0])
        ref = int(result[1]) # this ref is the corresponding row of city_df / the city that is closest to the input station
        out_df.at[ref, 'station'] = station_ref
        out_df.at[ref, 'distance'] = distance

out_df.to_csv('out.csv')