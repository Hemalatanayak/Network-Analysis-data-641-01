import csv
import os
import json
import sys
# Function to extract IMDb URIs from the CSV
def extract_imdb_uris(csv_file_path):
    imdb_uris = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            imdb_uri = row['IMDb_URI']
            imdb_uris.append(imdb_uri)
    return imdb_uris


# print(sys.path)

def create_director_directories(base_path, imdb_uris):
    os.makedirs(base_path, exist_ok=True)
    for imdb_uri in imdb_uris:
        dir_id = imdb_uri.split('/')[-2]
        dir_path = os.path.join(base_path, dir_id)
        os.makedirs(dir_path, exist_ok=True)

# print("b")

def save_director_credits(base_path, director_credits, dir_id):
    dir_path = os.path.join(base_path, dir_id)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, 'credits.json')
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(director_credits, file, indent=4)
        file.write('\n')

# Load the credit.json file for each director
def load_credit_json(dir_id):
    file_path = os.path.join('film-directors', dir_id, 'credits.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

