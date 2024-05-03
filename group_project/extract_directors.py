# This will list all names defined in utils, check for your function names

from utils import extract_imdb_uris,create_director_directories,save_director_credits
from imdb_scraper import get_full_credits_for_director
import os
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
# Get full credits for each director and save them if directory is empty
for imdb_uri in imdb_uris:
    dir_id = imdb_uri.split('/')[-2]
    director_path = os.path.join(base_directory, dir_id)

    # Ensure each director's directory is properly setup
    if not os.path.exists(director_path):
        os.makedirs(director_path)

    # Check if the director's directory is empty
    # Check if the director's directory is empty (excluding hidden files/directories)
    if not any(file.endswith('.json') for file in os.listdir(director_path)):
        try:
            full_credits = get_full_credits_for_director(dir_id)
            if full_credits:
                save_director_credits(base_directory, full_credits, dir_id)
                print(f"Data saved for director ID {dir_id}")
            else:
                print(f"No data found for director ID {dir_id}, fetched result was empty.")
        except Exception as e:
            print(f"Failed to fetch or save data for director ID {dir_id}. Error: {e}")
    else:
        print(f"Data already exists for director ID {dir_id} and directory is not empty.")


# # Get full credits for each director and save them
# for imdb_uri in imdb_uris:
#     dir_id = imdb_uri.split('/')[-2]
#     director_path = os.path.join(base_directory, dir_id)

#     # Check if the directory exists and is not empty
#     if os.path.exists(director_path) and os.listdir(director_path):
#         print(f"Data already exists for director ID {dir_id} and is not empty")
#     else:
#         full_credits = get_full_credits_for_director(dir_id)
#         if full_credits:
#             save_director_credits(base_directory, full_credits, dir_id)
#             print(f"Data saved for director ID {dir_id}")
#         else:
#             print(f"No data found for director ID {dir_id}")

# for imdb_uri in imdb_uris:
#     dir_id = imdb_uri.split('/')[-2]
#     full_credits = get_full_credits_for_director(dir_id)
#     if full_credits:
#         save_director_credits(base_directory, full_credits, dir_id)

# Get full credits for each director and save them
# for imdb_uri in imdb_uris:
#     dir_id = imdb_uri.split('/')[-2]
#     director_path = os.path.join(base_directory, dir_id)

#     # Initialize a flag to check if any file is empty
#     any_file_empty = False

#     # Check each file in the director's directory
#     if os.path.exists(director_path) and os.listdir(director_path):
#         for file in os.listdir(director_path):
#             file_path = os.path.join(director_path, file)
#             if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
#                 any_file_empty = True
#                 break

#     # If directory does not exist, is empty, or any file is empty
#     if not os.path.exists(director_path) or not os.listdir(director_path) or any_file_empty:
#         full_credits = get_full_credits_for_director(dir_id)
#         if full_credits:
#             save_director_credits(base_directory, full_credits, dir_id)
#             print(f"Data saved for director ID {dir_id}")
#         else:
#             print(f"No data found for director ID {dir_id}")
#     else:
#         print(f"Data already exists for director ID {dir_id} and all files are not empty.")