# Film Director Collaborative Network Analysis

## Overview
This project aims to analyze collaborative networks among renowned film directors, focusing on key collaborators and their roles. By examining patterns of collaboration and diversity in hiring practices, we seek to understand how these factors influence the U.S. film industry's creative landscape.

## Milestone-1: Data Extraction

### Data Source
The project starts by extracting relevant information(all details of directors and their movies) from a CSV file (`100_film_directors.csv`) containing data on directors and their movies.

### Code Description
The repository contains code for extracting director and movie information from the CSV file.

`imdb_scraper.py` - This script facillitates scraping of the directors and their movie.

`extract_directors.py` - This script organizes movie director data into a structured directory. It first creates a main directory called "film-directors" and then creates subdirectories for each director, naming them based on their unique dir_id. Next, it extracts IMDb URIs for each director from the CSV file, scrapes the corresponding IMDb pages for their movie information, and stores this data in a file named **credit.json** within each director's subdirectory.

`get_crew_data.py` - This script scrapes all the IMDb movie links (e.g., https://www.imdb.com/title/tt5104604/) from the ***credit.json*** file. It then stores all the crew details for each movie in separate files (***e.g., \film-directors\nm0000095\tt0061177_full_credits.json***).

`normalization.py` - This script standardizes all variations of cast and writing credits to their root roles. It saves these normalized credits in a directory named ***normalized_data*** inside each director's directory. The files inside normalized_data (***e.g., film-directors\nm0000095\normalized_data\tt0061177_full_credits.json***) contain all the normalized information. 

**Note:** This script also filters out the movie which are short and keeps only those movies which are longer than 70 min. The ***normalized_data*** directory contains only featured movies and the normalized crew information.

`sanity_check.ipynb` - This notebook contains answers to some of the research question. It is just to check whether data has been extracted correctly or not. The notebook is self explanatory.


## Getting Started
1. Clone this repository.
2. Ensure you have Python and the required packages installed (listed in `requirements.txt`).
3. Run the scripts *extract_directors.py*, *get_crew_data.py*, *normalization.py* to perform their respective task as explained above.


## Next Steps
Once the data extraction is complete, the next steps involve analyzing the extracted data to create the collaborative network and visualize the relationships among directors and their collaborators.


