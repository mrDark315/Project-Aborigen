from func.display_game import display_game_icons
from func.display_profile_games import display_profile_games

def next_page(ui):
    # Which data to use (HomePage or ProfilePage)
    if hasattr(ui, "filtered_games"):  # HomePage
        total_games = len(ui.filtered_games)
        display_function = display_game_icons
    elif hasattr(ui, "saved_games"):  # ProfilePage
        total_games = len(ui.saved_games)
        display_function = display_profile_games
    else:
        return

    max_pages = (total_games + 5) // 6

    if ui.current_page + 1 < max_pages:
        ui.current_page += 1
        print(f"➡️ Переход на страницу {ui.current_page + 1}/{max_pages}")
        display_function(ui)

def prev_page(ui):
    """Переключение на предыдущую страницу."""
    if hasattr(ui, "filtered_games"):
        display_function = display_game_icons
    elif hasattr(ui, "saved_games"):
        display_function = display_profile_games
    else:
        return

    if ui.current_page > 0:
        ui.current_page -= 1
        print(f"⬅️ Возвращение на страницу {ui.current_page + 1}")
        display_function(ui)
