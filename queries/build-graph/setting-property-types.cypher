// Convert from string date to Date (Same for Weather)
MATCH (w:Flight)
WITH [item in split(w.date, "/") | toInteger(item)] AS dateComponents
WITH date({day: dateComponents[0], month: dateComponents[1], year: dateComponents[2]}) AS date
MATCH (w:Flight)
SET w.date = date

MATCH (w:Weather)
WITH [item in split(w.date, "/") | toInteger(item)] AS dateComponents
WITH date({day: dateComponents[0], month: dateComponents[1], year: dateComponents[2]}) AS date
MATCH (w:Weather)
SET w.date = date

// connecting cities to weather events with new relation HAS_WEATHER
MATCH (c:City), (w:Weather), (s:Station)
WHERE (c)-[:NEARBY]-(s) AND (s)-[:OBSERVES]-(w)
MERGE (c)-[:HAS_WEATHER]->(w)

// data type conversions
MATCH (c:City)
SET c.lat = toFloat(c.lat)

MATCH (c:City)
SET c.long = toFloat(c.long)

MATCH (c:City)
SET c.population = toInteger(c.population)

MATCH (c:Airport)
SET c.lat = toFloat(c.lat)

MATCH (c:Airport)
SET c.long = toFloat(c.long)

MATCH (c:Station)
SET c.long = toFloat(c.long)

MATCH (c:Station)
SET c.lat = toFloat(c.lat)

MATCH (c:Station)
SET c.elevation = toFloat(c.elevation)

MATCH (c:Flight)
SET c.flightNumber = toInteger(c.flightNumber)

MATCH (c:Weather)
SET c.avgTemp = toFloat(c.avgTemp)

MATCH (c:Weather)
SET c.maxTemp = toFloat(c.maxTemp)

MATCH (c:Weather)
SET c.minTemp = toFloat(c.minTemp)

MATCH (c:Weather)
SET c.avgWindSpeed = toFloat(c.avgWindSpeed)

MATCH (c:Weather)
SET c.fastWindSpeed = toFloat(c.fastWindSpeed)

MATCH (c:Weather)
SET c.rainfall = toFloat(c.rainfall)

MATCH (c:Weather)
SET c.snowfall = toFloat(c.snowfall)

MATCH (c:Weather)
SET c.snowDepth = toFloat(c.snowDepth)

MATCH (c:Emission)
SET c.totalCO2 = toInteger(c.totalCO2)











