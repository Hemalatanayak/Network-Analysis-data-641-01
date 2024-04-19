from utils import load_credit_json
from imdb_scraper import get_full_crew_for_movie

import os
import json

# Define the base directory
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
        full_credits = get_full_crew_for_movie(title_id)
        # Store full_credits in a JSON file inside the director's directory
        dir_path = os.path.join(base_directory, dir_id)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, f"{title_id}_full_credits.json")
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(full_credits, file, indent=4)
        else:
            print(f"File already exists for {dir_id} - {title_id}. Skipping.")