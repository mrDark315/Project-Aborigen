from func.download_data import cached_games_data

def search_games(query):
    query = query.strip().lower()
    return [game for game in cached_games_data if query in game["name"].lower()]

def handle_search(ui):
    search_query = ui.search_bar.text().strip()
    ui.filtered_games = search_games(search_query) if search_query else cached_games_data
    ui.current_page = 0
    ui.grid_widget.setVisible(len(ui.filtered_games) > 0)
    ui.display_game_icons()

def delay_search(ui):
    ui.search_timer.start(1000)
    handle_search(ui)
