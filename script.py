import json

# Load the main game data
with open("store/data.json", "r", encoding="utf-8") as file:
    games = json.load(file)

filtered_games = []

for game in games:
    try:
        # Extract relevant data
        game_id = game.get("appid")
        name = game.get("name", "Unknown")
        img = game.get("img", "")

        # Handle Metacritic score (convert from string if needed)
        metacritic_data = game.get("metacritic", "{}")
        if isinstance(metacritic_data, str):
            try:
                metacritic_data = json.loads(metacritic_data.replace("'", "\""))
            except json.JSONDecodeError:
                metacritic_data = {}

        metacritic_score = metacritic_data.get("score", "N/A")

        # ✅ Fix: Handle controller support
        controller_support = game.get("controller_support", "").strip().lower()

        # Convert possible stringified JSON
        if isinstance(controller_support, str):
            try:
                controller_support = json.loads(controller_support.replace("'", "\""))
            except json.JSONDecodeError:
                pass

        # Ensure controller support has a valid value
        controller_support = controller_support if controller_support in ["full", "yes", "true", "enabled"] else "no"

        # Create filtered game object
        filtered_game = {
            "id": game_id,
            "name": name,
            "img": img,
            "metacritic_score": metacritic_score,
            "controller_support": controller_support  # ✅ Now correctly extracted
        }

        filtered_games.append(filtered_game)

    except (SyntaxError, ValueError, KeyError) as e:
        print(f"⚠️ Error processing {name}: {e}")

# Save the filtered data
output_file = "GameCardHomeData.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(filtered_games, file, indent=4, ensure_ascii=False)

print(f"✅ Data successfully saved to {output_file}")
