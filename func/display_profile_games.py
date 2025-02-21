import json
from PyQt5.QtWidgets import QWidget, QLabel
from components.GameCardProfile import GameCardProfile

def display_profile_games(ui: QWidget):
    try:
        with open("store/saved_games.json", "r", encoding="utf-8") as file:
            ui.saved_games = json.load(file)
        print(f"📂 List of saved games: {[game['name'] for game in ui.saved_games]}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("⚠️ saved_games.json was damaged or missing.")
        ui.saved_games = []

    ui.saved_games = [game for game in ui.saved_games if isinstance(game, dict)]

    # Clearing the grid before displaying new games
    for i in reversed(range(ui.grid_layout.count())):
        widget = ui.grid_layout.itemAt(i).widget()
        if widget:
            widget.setParent(None)
            widget.deleteLater()

    # Get the required games for the current page
    total_games = len(ui.saved_games)
    if total_games == 0:
        no_games_label = QLabel("No games found")
        no_games_label.setStyleSheet("color: #454C55; font-size: 40px; font-weight: bold;")
        ui.grid_layout.addWidget(no_games_label, 0, 0, 1, 3)
    else:
        start_index = ui.current_page * 6
        end_index = min(start_index + 6, len(ui.saved_games))
        games_to_display = ui.saved_games[start_index:end_index]

        row, col = 0, 0
        max_cols = 3
        for game in games_to_display:
            game_widget = GameCardProfile(game, ui)
            ui.grid_layout.addWidget(game_widget, row, col)

            col += 1
            if col >= max_cols:
                col = 0
                row += 1

    # Turn navigation buttons on/off
    ui.left_arrow.setEnabled(ui.current_page > 0)
    ui.right_arrow.setEnabled((ui.current_page + 1) * 6 < len(ui.saved_games))
