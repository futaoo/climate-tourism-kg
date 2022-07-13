# script to connect a weather station to a nearby city based on X, Y co-ordinates

from scipy import spatial
import pandas as pd
import csv

city_df = pd.read_csv("unique-stations.csv", usecols=[2,3])
city_records = city_df.to_records(index=False)
cities = city_records.tolist()

tree = spatial.KDTree(cities)
out_df = pd.read_csv("unique-stations.csv", usecols=[0,1,2,3,4])

with open('uscities-over10k.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        city_ref = row[0]
        lat = float(row[3])
        lng = float(row[4])
        result = tree.query([(lat,lng)], k=1, eps=10)
        distance = float(result[0])
        ref = int(result[1]) # this ref is the corresponding row of city_df / the city that is closest to the input station
        out_df.at[ref, 'city'] = city_ref
        out_df.at[ref, 'distance'] = distance

out_df.to_csv('out.csv')