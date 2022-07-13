import csv
import json
import requests
import geopy.distance
import pandas as pd

headers = {
    'Authorization': 'Bearer F5BMHGYHRD4H4NNY081RB7BF09KZ',
    'Content-Type': 'application/x-www-form-urlencoded',
}
distancesList = []
# Read out.csv line by line, take co-ords for departure and arrival airports, 
df = pd.read_csv('out.csv')
df = df.reset_index()

for index, row in df.iterrows():
    departure = (df.at[index, 'lat1'], df.at[index, 'long1'])
    arrival = (df.at[index, 'lat2'], df.at[index, 'long2'])
    calculated_distance = int(geopy.distance.distance(departure, arrival).km)
    distancesList.append(calculated_distance)
    if len(distancesList) == 10:
        distances = tuple(distancesList)
        data = '[{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}},{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}},{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}},{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}},{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}},{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}},{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}},{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}},{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}},{"emission_factor": "passenger_flight-route_type_na-aircraft_type_na-distance_gt_300mi_lt_2300mi-class_na-rf_na","parameters": {"passengers": 100,"distance": %s,"distance_unit": "km"}}]' % distances
        response = requests.post('https://beta3.api.climatiq.io/batch', headers=headers, data=data)
        obj = json.loads(response.content)
        for i in range(10):
            chosen_data = [df.at[i, 'flight_iata'],obj["results"][i]["co2e"],obj["results"][i]["co2e_unit"],obj["results"][i]["emission_factor"]["source"],obj["results"][i]["emission_factor"]["region"],obj["results"][i]["emission_factor"]["category"],obj["results"][i]["emission_factor"]["lca_activity"]]
            with open('emissions2.csv', 'a') as csvfile:
                temp = csv.writer(csvfile, delimiter=',')
                temp.writerow(chosen_data)
        distancesList = []
