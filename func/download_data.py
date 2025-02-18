import orjson
import os
import random

cached_games_data = []
cached_games_dict = {}

def load_json_data(file_path="store/data.json"):
    global cached_games_data, cached_games_dict

    if os.path.exists(file_path):
        try:
            with open(file_path, "rb") as file:
                cached_games_data = orjson.loads(file.read())
                random.shuffle(cached_games_data)
                cached_games_dict = {game["name"].lower(): game for game in cached_games_data}
                print(f"✅ JSON has been uploaded: {len(cached_games_data)} games.")
        except orjson.JSONDecodeError:
            print(f"⚠️ Error: File {file_path} damaged. Use an empty list.")
            cached_games_data = []
            cached_games_dict = {}
    else:
        print(f"⚠️ Warning: File {file_path} not found. Use an empty list.")
        cached_games_data = []
        cached_games_dict = {}

load_json_data()
