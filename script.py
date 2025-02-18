import json
import ast

# Открываем JSON-файл
with open("store/data.json", "r", encoding="utf-8") as file:
    games = json.load(file)

filtered_games = []

for game in games:
    try:
        # Парсим поле developer, если оно есть
        developers = ast.literal_eval(game["developer"]) if game["developer"] else []

        # Собираем нужные данные
        filtered_game = {
            "id": game["appid"],
            "name": game["name"],
            "developers": developers
        }

        filtered_games.append(filtered_game)
    except (SyntaxError, ValueError, KeyError) as e:
        print(f"Ошибка при обработке {game['name']}: {e}")

# Сохраняем в новый JSON-файл
output_file = "store/SideFilterData.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(filtered_games, file, indent=4, ensure_ascii=False)

print(f"Данные сохранены в {output_file}")
