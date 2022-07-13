// Case 1: Airline CO2 Emissions

    MATCH (a:Airline)-[:CARRIES]->(f)-[:EMITS]->(e:Emission)
    RETURN a.name, sum(e.totalCO2) as totalEmissions
    ORDER BY totalEmissions DESC LIMIT 5

// Flight with Max Emissions

    MATCH (f:Flight)-[:EMITS]->(e:Emission)
    RETURN f.iata, max(e.totalCO2) as maxEmissions
    ORDER BY maxEmissions DESC LIMIT 1


// Case 2: Let's Go Skiing

    MATCH (w:Weather)
    WITH max(w.snowDepth) AS maxSnowDepth
    MATCH (c:City)-[:HAS_WEATHER]-(n:Weather {snowDepth: maxSnowDepth})
    RETURN c, n

    MATCH (c:City)-[r:HAS_WEATHER]-(w)
    WHERE w.date > "2021-12-31" AND w.date < "2022-01-16"
    RETURN c.name, sum(w.snowDepth) as totalSnowDepth
    ORDER BY totalSnowDepth DESC LIMIT 1


// Case 3: Busy Airports

    MATCH (c)-[:ARRIVES]-(a:Airport)-[:DEPARTS]-(f)
    RETURN a, COLLECT(a) as leastBusyAirports
    ORDER BY SIZE(leastBusyAirports) ASC LIMIT 3


// pageRank 

    CALL gds.pageRank.stream(airportsAndFlights)
    YIELD nodeId, score
    RETURN gds.util.asNode(nodeId).name AS name, score
    ORDER BY score DESC, name ASC


// Case 4: Route Distance

    MATCH (w:Weather {date: "2022-01-01"})
    WITH max(w.maxTemp) AS highestTemperature
    MATCH (c:City)-[a:NEARBY]-(s:Station)-[:OBSERVES]-(z:Weather
        {maxTemp: highestTemperature})
    RETURN z.station, z.date, highestTemperature, a.distance, c.name


    MATCH (a:City)-[b:NEARBY]-(c)-[d:DEPARTS]-(e:Flight {iata: AC3049})
        -[f:ARRIVES]-(g)-[h:NEARBY]-(i:City)
    RETURN b.distance + d.distance + h.distance


