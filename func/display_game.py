from components.GameCardHome import GameCardHome

def display_game_icons(ui):
    while ui.grid_layout.count():
        widget = ui.grid_layout.takeAt(0).widget()
        if widget:
            widget.deleteLater()

    total_games = len(ui.filtered_games)
    start_index = ui.current_page * 6
    end_index = min(start_index + 6, total_games)
    games_to_display = ui.filtered_games[start_index:end_index]

    # Print which games are being displayed (Debugging)
    print(f"📄 Showing games {start_index + 1} to {end_index} out of {total_games}")

    row, col = 0, 0
    for game in games_to_display:
        print(f"🎮 Adding game: {game['name']}")
        game_widget = GameCardHome(game, ui)
        ui.grid_layout.addWidget(game_widget, row, col)
        col += 1
        if col > 2:
            col = 0
            row += 1

    # Enable/Disable Arrows based on pages
    ui.left_arrow.setEnabled(ui.current_page > 0)
    ui.right_arrow.setEnabled((ui.current_page + 1) * 6 < total_games)