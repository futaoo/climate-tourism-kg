# Improving Tourism Recommendation from Climate Data Using Knowledge Graphs



# About
This repository covers the implementation work done as part of the journal manuscript:
>J. Pierse, J. Wu, F. Orlandi, D. O'Sullivan, and S. Dev, **Improving Tourism Recommendation from Climate Data Using Knowledge Graphs**, *[UNDER REVIEW]*.

# Abstract
A Knowledge Graph is a type of knowledge representation that utilises a graph structure to connect and relate data of different types. The Climate-Tourism domain is data-rich with a vast amount of data generated everyday. Knowledge Graphs offer benefits in relating vast amounts of data but are underutilised in this domain.

This project aims to develop a Knowledge Graph in the Climate-Tourism domain, focusing on historical flights in the geographic area of North America. Climate data is sourced from over 5,000 weather stations across the United States and is integrated with flight data of over 100,000 domestic flights to provide a knowledge base that displays the relationship between weather and flights. Further data is integrated to provide CO2 emission estimations for flights to further demonstrate how climate-related data can be utilised in the modern context of climate change.

# Installation

## Note: There are two methods to install this project. Method 1 is the fastest way of seeing the graph in your browser without any installation. Method 2 runs locally on your desktop.

### Method 1 (fastest):

1. Navigate to [this](https://csgitlab.ucd.ie/jarrettpierse/fyp_climate_tourism_kg/-/blob/master/user-survey/fyp-survey.pdf) part of the repository.

2. Follow the step-by-step PDF for the user experience survey. The access URL, username and password are provided in this PDF.

3. If you have any issues connecting (this may happen as the cloud database is paused after 3 days of inactivity), please contact me via email jarrett.pierse@ucdconnect.ie


### Method 2 (slowest):

1. Neo4j Desktop is required to run the .dump dataset. This can be downloaded from [here](https://neo4j.com/download/). 

2. Once installed, create a new project and select 'Add' > 'File' and select one of the .dump files located [here](https://csgitlab.ucd.ie/jarrettpierse/fyp_climate_tourism_kg/-/tree/master/neo4j/dumps).

3. In the 'File' window at the bottom of your project, hover over the .dump file and select the options (...)

4. Select 'Create new DBMS from dump' and name the DB as appropriate.

5. Wait for the DBMS to load 

6. Start the database by selecting 'Start' when hovering over the newly created database.

7. Open the local Neo4j broswer by selecting 'Open'

8. From here you can query the graph directly through the built-in CYPHER command line.
