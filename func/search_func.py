import json
import os
from func.download_data import cached_games_data

def handle_search(ui):
    ui.filtered_games = cached_games_data
    ui.current_page = 0
    ui.grid_widget.setVisible(len(ui.filtered_games) > 0)
    ui.display_game_icons()

def delay_search(ui):
    ui.search_timer.start(1000)
    handle_search(ui)
