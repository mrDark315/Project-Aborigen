import json
from collections import defaultdict

with open("store/GameCardHomeData.json", "r", encoding="utf-8") as file:
    cached_games_data = json.load(file)

cached_games_dict = {game["name"].lower(): game for game in cached_games_data}

# Optimized index for fast searching
search_index = defaultdict(set)

for game in cached_games_data:
    name_lower = game["name"].lower()
    words = name_lower.split()  # Breaking the title into words
    for word in words:
        if len(word) >= 3:  # We index only words from 3 characters
            search_index[word].add(name_lower)

        for i in range(len(word) - 2):
            substring = word[i:i + 3]
            search_index[substring].add(name_lower)

search_cache = {}

def search_games(query):
    query = query.strip().lower()

    if len(query) < 3:
        return []

    if query in search_cache:
        return search_cache[query]

    matched_names = set()

    for key in search_index:
        if query in key:  # Check if the query is contained in the index key
            matched_names.update(search_index[key])

    # Convert to a list of game objects
    result = [cached_games_dict[name] for name in matched_names] if matched_names else []

    # Cache the result
    search_cache[query] = result
    return result

def handle_search(ui):
    search_query = ui.search_bar.text().strip()
    if not cached_games_data:
        print("⚠️ Error: Game data not loaded!")
        return

    if search_query:
        ui.filtered_games = search_games(search_query)
    else:
        ui.filtered_games = cached_games_data[:]

    ui.current_page = 0
    ui.grid_widget.setVisible(len(ui.filtered_games) > 0)
    ui.display_game_icons()

def delay_search(ui):
    ui.search_timer.start(2000)
    handle_search(ui)
