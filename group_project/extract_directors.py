# This will list all names defined in utils, check for your function names

from utils import extract_imdb_uris,create_director_directories,save_director_credits
from imdb_scraper import get_full_credits_for_director

# Read directors from CSV and extract IMDb URIs

# Path to the CSV file
csv_file_path = '100_film_directors.csv'

def get_full_credits_for_directors(imdb_uris):
    full_credits_list = []
    for imdb_uri in imdb_uris:
        dir_id = imdb_uri.split('/')[-2]
        full_credits = get_full_credits_for_director(dir_id)
        if full_credits:
            full_credits_list.append(full_credits)
    return full_credits_list

# Define the base directory
base_directory = 'film-directors'

# Extract IMDb URIs
imdb_uris = extract_imdb_uris(csv_file_path)

# Create directories for each director
create_director_directories(base_directory, imdb_uris)

# Get full credits for each director and save them
for imdb_uri in imdb_uris:
    dir_id = imdb_uri.split('/')[-2]
    full_credits = get_full_credits_for_director(dir_id)
    if full_credits:
        save_director_credits(base_directory, full_credits, dir_id)

