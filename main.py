from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
import os, sys, json, requests
from func.download_data import cached_games_data
from func.search_func import handle_search, delay_search
from components.SearchBar import SearchBar
from components.ProfileButton import ProfileButton
from components.CreatedByButton import CreatedByButton
from components.NavArrows import AnimatedArrowButton
from components.SideFilter import SideFilter
from components.GameCardHome import GameCardHome

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Responsive Window Size
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        MainWindow.resize(int(screen.width() * 0.8), int(screen.height() * 0.8))
        MainWindow.setMinimumSize(QSize(1600, 970))
        MainWindow.setMaximumSize(QSize(1920, 1080))

        # Main Widget
        self.main = QtWidgets.QWidget(MainWindow)
        self.main.setStyleSheet("background-color: #0E1621;")
        self.main.setObjectName("main")

        # Main Layout (Vertical)
        self.layout = QtWidgets.QVBoxLayout(self.main)

        # Search Layout (Horizontal)
        self.search_filter_layout = QtWidgets.QHBoxLayout()
        self.search_filter_layout.setAlignment(Qt.AlignCenter)
        self.search_filter_layout.setSpacing(50)

        # Created by button
        self.created_by_btn = CreatedByButton(self)

        # Search Bar
        self.search_bar = SearchBar(self)

        # Profile button
        self.profile_btn = ProfileButton(self)

        # Add Search Bar to Layout
        self.search_filter_layout.addWidget(self.created_by_btn)
        self.search_filter_layout.addWidget(self.search_bar)
        self.search_filter_layout.addWidget(self.profile_btn)

        # Grid Navigation Layout (Arrows + Game Grid)
        self.grid_navigation_layout = QtWidgets.QHBoxLayout()
        self.grid_navigation_layout.setAlignment(Qt.AlignCenter)

        # Left Arrow Button
        self.left_arrow = AnimatedArrowButton("img/Arrow_Left.png", self, "left")

        # Right Arrow Button
        self.right_arrow = AnimatedArrowButton("img/Arrow_Right.png", self, "right")

        # Side Filter Layout
        self.side_filter = SideFilter(self)

        # Grid Layout for Displaying Games
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setSpacing(20)
        self.grid_widget = QtWidgets.QWidget()
        self.grid_widget.setLayout(self.grid_layout)
        self.grid_widget.setVisible(False)

        # Add to Grid Navigation Layout
        self.grid_navigation_layout.addWidget(self.side_filter)
        self.grid_navigation_layout.addWidget(self.left_arrow)
        self.grid_navigation_layout.addWidget(self.grid_widget)
        self.grid_navigation_layout.addWidget(self.right_arrow)

        # Add to Main Layout
        self.layout.addLayout(self.search_filter_layout)
        self.layout.addLayout(self.grid_navigation_layout)

        MainWindow.setCentralWidget(self.main)

        # Load Game Data
        self.filtered_games = cached_games_data[:]
        self.current_page = 0
        handle_search(self)

        # Connect search bar & filter event
        self.search_timer = QtCore.QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(lambda: handle_search(self))
        self.search_bar.textChanged.connect(lambda: delay_search(self))

    def display_game_icons(self):
        while self.grid_layout.count():
            widget = self.grid_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        total_games = len(self.filtered_games)
        start_index = self.current_page * 6
        end_index = min(start_index + 6, total_games)
        games_to_display = self.filtered_games[start_index:end_index]

        # Print which games are being displayed (Debugging)
        print(f"📄 Showing games {start_index + 1} to {end_index} out of {total_games}")

        row, col = 0, 0
        for game in games_to_display:
            print(f"🎮 Adding game: {game['name']}")
            game_widget = GameCardHome(game, self)
            self.grid_layout.addWidget(game_widget, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Enable/Disable Arrows based on pages
        self.left_arrow.setEnabled(self.current_page > 0)
        self.right_arrow.setEnabled((self.current_page + 1) * 6 < total_games)

    # def load_favorites(self):
    #     if os.path.exists("store/favorites.json"):
    #         try:
    #             with open("store/favorites.json", "r", encoding="utf-8") as file:
    #                 return json.load(file)
    #         except json.JSONDecodeError:
    #             return {}  # Return empty if file is corrupted
    #     return {}

    # def save_favorites(self, favorites):
    #     with open("store/favorites.json", "w", encoding="utf-8") as file:
    #         json.dump(favorites, file, indent=4, ensure_ascii=False)

    # def hide_widgets_in_layout(self, layout):
    #     for i in range(layout.count()):
    #         widget = layout.itemAt(i).widget()
    #         if widget:
    #             widget.setVisible(False)

    # def show_widgets_in_layout(self, layout):
    #     for i in range(layout.count()):
    #         widget = layout.itemAt(i).widget()
    #         if widget:
    #             widget.setVisible(True)

    # def open_profile(self):
    #     # Change data source to `favorites.json`
    #     self.perform_search("store/favorites.json")

    #     # Keep all UI elements visible (DO NOT hide filters, search bar, or arrows)
    #     self.show_widgets_in_layout(self.search_filter_layout)
    #     self.show_widgets_in_layout(self.grid_navigation_layout)

    #     print("🔹 Switched to profile mode. Showing only favorite games.")

    # def remove_from_favorites(self, game):
    #     favorites = self.load_favorites()

    #     game_id = str(game["appid"])

    #     if game_id in favorites:
    #         del favorites[game_id]
    #         self.save_favorites(favorites)
    #         print(f"❌ Removed {game['name']} from favorites.")

    #     self.open_profile()  # Refresh the profile section in the same window


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
