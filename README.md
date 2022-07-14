# Improving Tourism Recommendation from Climate Data Using Knowledge Graphs



# About
This repository covers the implementation work done as part of the journal manuscript:
>J. Pierse, J. Wu, F. Orlandi, D. O'Sullivan, and S. Dev, **Improving Tourism Recommendation from Climate Data Using Knowledge Graphs**, *[UNDER REVIEW]*.

# Abstract
A Knowledge Graph is a type of knowledge representation that utilises a graph structure to connect and relate data of different types. The Climate-Tourism domain is data-rich with a vast amount of data generated everyday. Knowledge Graphs offer benefits in relating vast amounts of data but are underutilised in this domain.

This project aims to develop a Knowledge Graph in the Climate-Tourism domain, focusing on historical flights in the geographic area of North America. Climate data is sourced from over 5,000 weather stations across the United States and is integrated with flight data of over 100,000 domestic flights to provide a knowledge base that displays the relationship between weather and flights. Further data is integrated to provide CO2 emission estimations for flights to further demonstrate how climate-related data can be utilised in the modern context of climate change.

# Installation

## Note: this repository provides source scripts that serve mostly as illustrations for the journal manuscript's methodology section. To install our Climate-Toursim Knowledge Graph even faster, we suggest following the steps below, which include pre-configured Neo4j dumps for usage with the Neo4J Desktop.. 


1. Neo4j Desktop is required to run the .dump dataset. This can be downloaded from [here](https://neo4j.com/download/). 

2. Once installed, create a new project and select 'Add' > 'File' and select one of the .dump files located [here](https://github.com/futaoo/climate-tourism-kg/tree/main/neo4j-dumps).

3. In the 'File' window at the bottom of your project, hover over the .dump file and select the options (...)

4. Select 'Create new DBMS from dump' and name the DB as appropriate.

5. Wait for the DBMS to load 

6. Start the database by selecting 'Start' when hovering over the newly created database.

7. Open the local Neo4j broswer by selecting 'Open'

8. From here you can query the graph directly through the built-in CYPHER command line.
