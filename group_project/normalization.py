import os
import json
from imdb_scraper import normalize_movie_role, normalize_movie_subrole

# Path to the main directory containing subdirectories for each director
main_directory = r'C:\Users\nayak\OneDrive\Desktop\Network-Analysis-data-641-01\group_project\film-directors'

# Iterate through each subdirectory
for director_dir in os.listdir(main_directory):
    director_path = os.path.join(main_directory, director_dir)
    if os.path.isdir(director_path):
        normalized_data_dir = os.path.join(director_path, 'normalized_data')
        os.makedirs(normalized_data_dir, exist_ok=True)  # Create normalized_data directory if it doesn't exist
        for file_name in os.listdir(director_path):
            if file_name.startswith('tt') and file_name.endswith('.json'):
                file_path = os.path.join(director_path, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        if not data.get('full_credits'):
                            print(f"Skipping empty file: {file_path}")
                            continue
                        for full_credit in data['full_credits']:
                            original_role = full_credit['role']
                            normalized_role = normalize_movie_role(original_role)
                            full_credit['normalized role'] = normalized_role
                            crew = full_credit.get('crew', [])  # Extract the 'crew' list from each 'full_credits' entry
                            normalize_movie_subrole(crew)
                    
                    # Save the normalized data to a new JSON file in the normalized_data directory
                    new_file_path = os.path.join(normalized_data_dir, file_name)
                    with open(new_file_path, 'w', encoding='utf-8') as new_file:
                        json.dump(data, new_file, indent=4)
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

