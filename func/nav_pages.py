def next_page(self):
        total_games = len(self.filtered_games)
        max_pages = (total_games + 5) // 6

        if total_games == 0:
            print("⚠️ Нет игр для перелистывания!")
            return

        if self.current_page + 1 < max_pages:
            self.current_page += 1
            print(f"➡️ Change page {self.current_page + 1}/{max_pages}")
            self.display_game_icons()

def prev_page(self):
    if self.current_page > 0:
        self.current_page -= 1
        print(f"⬅️ Change page {self.current_page + 1}")
        self.display_game_icons()