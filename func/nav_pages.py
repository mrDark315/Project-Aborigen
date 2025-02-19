from func.display_game import display_game_icons

def next_page(self):
        total_games = len(self.filtered_games)
        max_pages = (total_games + 5) // 6

        if self.current_page + 1 < max_pages:
            self.current_page += 1
            print(f"➡️ Change page {self.current_page + 1}/{max_pages}")
            display_game_icons(self)

def prev_page(self):
    if self.current_page > 0:
        self.current_page -= 1
        print(f"⬅️ Change page {self.current_page + 1}")
        display_game_icons(self)