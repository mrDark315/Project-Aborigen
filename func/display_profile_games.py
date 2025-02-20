import json
from PyQt5.QtWidgets import QWidget
from components.GameCardProfile import GameCardProfile

def display_profile_games(ui: QWidget):
    try:
        with open("store/saved_games.json", "r", encoding="utf-8") as file:
            saved_games = json.load(file)
        print(f"📂 Загруженные сохраненные игры перед обработкой: {saved_games}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("⚠️ Файл saved_games.json отсутствует или поврежден, загружаем пустой список.")
        saved_games = []

    saved_games = [game for game in saved_games if isinstance(game, dict)]

    print(f"📂 Итоговый список игр после проверки: {saved_games}")

    for i in reversed(range(ui.grid_layout.count())):
        widget = ui.grid_layout.itemAt(i).widget()
        if widget:
            widget.setParent(None)
            widget.deleteLater()

    row, col = 0, 0
    max_cols = 3
    for game in saved_games:
        game_widget = GameCardProfile(game, ui)
        ui.grid_layout.addWidget(game_widget, row, col)

        col += 1
        if col >= max_cols:
            col = 0
            row += 1

    print(f"🎮 Отображаемые игры в профиле: {[game['name'] for game in saved_games]}")
