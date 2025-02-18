import json
import os
import random

cached_games_data = []

def load_json_data(file_path="data.json"):
    global cached_games_data

    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                games = json.load(file)
                cached_games_data = list(games.values()) if isinstance(games, dict) else games
                random.shuffle(cached_games_data)
                print(f"✅ JSON has been uploaded: {len(cached_games_data)} games (random).")
        except json.JSONDecodeError:
            print(f"⚠️ Error: File {file_path} damaged. Use an empty list.")
            cached_games_data = []
    else:
        print(f"⚠️ Warning: File {file_path} not found. Use an empty list.")
        cached_games_data = []

load_json_data()
