# Film Director Collaborative Network Analysis

## Getting Started
1. Clone this repository.
2. Ensure you have Python and the required packages installed (listed in `requirements.txt`).
3. Run the scripts *extract_directors.py*, *get_crew_data.py*, *normalization.py* to perform their respective task as explained above.

## Overview
This project aims to analyze collaborative networks among renowned film directors, focusing on key collaborators and their roles. By examining patterns of collaboration and diversity in hiring practices, we seek to understand how these factors influence the U.S. film industry's creative landscape.

**It addresses the following research questions:**

1) What is the distribution of entities in the director-crew dataset:
* Number of featured movies?
* Number of directors, number movies per director, and average number of movies per director?
* Number of crews?
* Number of roles and frequency of each role?

2) How will you characterize the film-director network? What are the properties (degree dist., average shortest path length, triangles aka clustering coefficient, density/sparcity)?
Pick two questions:

3) Investigate and quantify how directors have influenced the careers of crew members. Clue: consider mapping the careers of crew members over time and see if they experienced significant success after working with a particular director. What directors have had the most influence on crew members?

4) Measure how roles of crew members fluctuate

## Steps to address the questions
To address these research question one need to follow these 4 steps as follows:

* Data Extraction
* Network Generation
* Network Visualization
* Analysis

### Data Source
The project starts by extracting relevant information(all details of directors and their movies) from a CSV file (`100_film_directors.csv`) containing data on directors and their movies.

### Data Extraction
The repository contains code for extracting director and movie information from the CSV file.

`imdb_scraper.py` - This script facillitates scraping of the directors and their movie.

`extract_directors.py` - This script organizes movie director data into a structured directory. It first creates a main directory called "film-directors" and then creates subdirectories for each director, naming them based on their unique dir_id. Next, it extracts IMDb URIs for each director from the CSV file, scrapes the corresponding IMDb pages for their movie information, and stores this data in a file named **credit.json** within each director's subdirectory.

`get_crew_data.py` - This script scrapes all the IMDb movie links (e.g., https://www.imdb.com/title/tt5104604/) from the ***credit.json*** file. It then stores all the crew details for each movie in separate files (***e.g., \film-directors\nm0000095\tt0061177_full_credits.json***).

`normalization.py` - This script standardizes all variations of cast and writing credits to their root roles. It saves these normalized credits in a directory named ***normalized_data*** inside each director's directory. The files inside normalized_data (***e.g., film-directors\nm0000095\normalized_data\tt0061177_full_credits.json***) contain all the normalized information. 

**Note:** This script also filters out the movie which are short and keeps only those movies which are longer than 70 min. The ***normalized_data*** directory contains only featured movies and the normalized crew information.



## Network Generation and Visualization
The Director-Crew network was constructed using the NetworkX library, as documented in `research_question.ipynb`, and saved in the ***network.graphml*** format. Subsequently, this `.graphml` file was visualized using an external platform, Gephi, to facilitate detailed analysis and presentation.

## Analysis
`research_question.ipynb` - This notebook contains answers to all of the research questions. The notebook is self-explanatory.

