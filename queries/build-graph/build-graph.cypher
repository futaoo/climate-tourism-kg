// FYP Survey Queries in order:

LOAD CSV WITH HEADERS FROM 'file:///unique_airports.csv' AS line with line WHERE line.departure_airport IS NOT NULL
MERGE (a:Airport {lat: line.latitude, long: line.longitude, iata: line.departure_iata, icao: line.departure_icao, name: line.departure_airport})

LOAD CSV WITH HEADERS FROM 'file:///airports_cities.csv' AS line with line WHERE line.CITY IS NOT NULL
MERGE (c:City {name: line.CITY, state: line.STATE, population: line.POPULATION, lat: line.LAT, long: line.LONG, airp: line.AIRPORT})

MATCH (a:Airport), (c:City)
WHERE a.iata = c.airp
MERGE (a)<-[:NEARBY]->(c)

MATCH (c:City)
REMOVE c.airp

LOAD CSV WITH HEADERS FROM 'file:///weather-stations.csv' AS line with line WHERE line.STATION IS NOT NULL
MERGE (s:Station {station: line.STATION, name: line.NAME, lat: line.LATITUDE, long: line.LONGITUDE, elevation: line.ELEVATION})

LOAD CSV WITH HEADERS FROM 'file:///city_station.csv' AS line with line WHERE line.STATION IS NOT NULL
MATCH (s:Station), (c:City)
WHERE s.station = line.STATION AND line.CITY = c.name
MERGE (s)<-[:NEARBY]->(c)

MATCH (s:Station), (c:City)
WHERE s.station = c.station
MERGE (s)<-[:NEARBY]->(c)

MATCH (c:City)
REMOVE c.station

LOAD CSV WITH HEADERS FROM 'file:///unique_airlines.csv' AS line with line WHERE line.airline_name IS NOT NULL
MERGE (a:Airline {name: line.airline_name, icao: line.airline_icao})

LOAD CSV WITH HEADERS FROM 'file:///unique_flights_jan22-sample.csv' AS line with line WHERE line.departure_airport IS NOT NULL
MERGE (f:Flight {date: line.flight_date, departure: line.departure_iata, arrival: line.arrival_iata, takeoff: line.takeoff_time, flightNumber: line.flight_number, iata: line.flight_iata, icao: line.flight_icao, airline: line.airline_icao})


MATCH (f:Flight), (a:Airline)
WHERE f.airline = a.icao
MERGE (a)-[:CARRIES]->(f)

MATCH(f:Flight), (a:Airport)
WHERE f.departure = a.iata
MERGE (f)-[:DEPARTS]->(a)

MATCH(f:Flight), (a:Airport)
WHERE f.arrival = a.iata
MERGE (f)-[:ARRIVES]->(a)

LOAD CSV WITH HEADERS FROM 'file:///emissions-sample.csv' AS line with line WHERE line.departure IS NOT NULL
MERGE (e:Emission {totalCO2: line.emissions, unit: line.unit, factor: line.factor, region: line.region, category: line.category, activity: line.lca_activity, departure: line.departure, arrival: line.arrival})

MATCH (e:Emission), (f:Flight)
WHERE e.departure = f.departure AND e.arrival = f.arrival
MERGE (f)-[:EMITS]->(e)


MATCH (e:Emission)
REMOVE e.arrival

MATCH (e:Emission)
REMOVE e.departure

LOAD CSV WITH HEADERS FROM 'file:///daily-summaries-jan22-sample.csv' AS line with line WHERE line.STATION IS NOT NULL
MERGE (w:Weather {station: line.STATION, date: line.DATE, avgWindSpeed: line.AWND, rainfall: line.PRCP, snowfall: line.SNOW, snowDepth: line.SNWD, avgTemp: line.TAVG, maxTemp: line.TMAX, minTemp: line.TMIN, fastWindSpeed: line.WSF2})

MATCH (w:Weather), (s:Station)
WHERE s.station = w.station
MERGE (s)-[:OBSERVES]->(w)

MATCH (a:Airport) , (s:Station), (c:City)
WHERE (s)-[:NEARBY]->(c) AND (a)-[:NEARBY]->(c)
MERGE (s)<-[:NEARBY]->(a)




