from func.download_data import *

def search_games(query):
    query = query.strip().lower()
    return [cached_games_dict[key] for key in cached_games_dict if query in key]

def handle_search(ui):
    search_query = ui.search_bar.text().strip()
    if not cached_games_data:
        print("⚠️ Ошибка: Данные игр не загружены!")
        return

    if search_query:
        ui.filtered_games = search_games(search_query)
    else:
        ui.filtered_games = cached_games_data[:]
    ui.current_page = 0
    ui.grid_widget.setVisible(len(ui.filtered_games) > 0)
    ui.display_game_icons()

def delay_search(ui):
    ui.search_timer.start(1000)
    handle_search(ui)
