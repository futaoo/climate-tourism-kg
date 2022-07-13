# Python script to filter the flights by unique values as some flights are carried by mulitple airlines

import pandas as pd

record = pd.read_csv('flights2.csv')

print(record.drop_duplicates(subset=['flight_date', 'departure_airport', 'departure_icao', 'departure_iata', 'departure_time', 'arrival_airport', 'arrival_icao', 'arrival_iata']))

new_rec = record.drop_duplicates(subset=['flight_date', 'departure_airport', 'departure_icao', 'departure_iata', 'departure_time', 'arrival_airport', 'arrival_icao', 'arrival_iata'])

new_rec.to_csv('unique_flights2.csv', index=False)