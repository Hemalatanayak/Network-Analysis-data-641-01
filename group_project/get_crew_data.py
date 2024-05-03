from utils import load_credit_json
from imdb_scraper import get_full_crew_for_movie

import os
import json

def is_file_empty(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content.strip() == '{}'  # Check if the content is only {}

base_directory = 'film-directors'

# Extract title IDs from credit.json files
for director in os.listdir(base_directory):
    dir_id = director
    try:
        credit_json = load_credit_json(dir_id)
    except FileNotFoundError:
        print(f"No credit.json file found for director: {dir_id}. Skipping.")
        continue

    for movie in credit_json['credits']:
        title_id = movie['uri'].split('/')[-2]
        # Define the path for the full credits JSON file
        dir_path = os.path.join(base_directory, dir_id)
        file_path = os.path.join(dir_path, f"{title_id}_full_credits.json")
        
        # Check if the file exists and is empty or contains only {}
        if os.path.exists(file_path) and is_file_empty(file_path):
            print(f"File {file_path} is empty or. Downloading again...")

            full_credits = get_full_crew_for_movie(title_id)
            if full_credits:
                os.makedirs(dir_path, exist_ok=True)
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(full_credits, file, indent=4)
                    print(f"Data saved for {dir_id} - {title_id}.")
            else:
                print(f"Failed to fetch full credits for {dir_id} - {title_id}. Skipping.")


# # Define the base directory
# base_directory = 'film-directors'

# # Extract title IDs from credit.json files
# for director in os.listdir(base_directory):
#     dir_id = director
#     try:
#         credit_json = load_credit_json(dir_id)
#     except FileNotFoundError:
#         print(f"No credit.json file found for director: {dir_id}. Skipping.")
#         continue

#     for movie in credit_json['credits']:
#         title_id = movie['uri'].split('/')[-2]
#         # Define the path for the full credits JSON file
#         dir_path = os.path.join(base_directory, dir_id)
#         file_path = os.path.join(dir_path, f"{title_id}_full_credits.json")
        
#         # Check if the file exists and is not empty
#         if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
#             print(f"File already exists and is not empty for {dir_id} - {title_id}. Skipping.")
#             continue
        
#         # Fetch full credits if the file is empty or does not exist
#         full_credits = get_full_crew_for_movie(title_id)
#         if full_credits:
#             os.makedirs(dir_path, exist_ok=True)
#             with open(file_path, 'w', encoding='utf-8') as file:
#                 json.dump(full_credits, file, indent=4)
#                 print(f"Data saved for {dir_id} - {title_id}.")
#         else:
#             print(f"Failed to fetch full credits for {dir_id} - {title_id}. Skipping.")