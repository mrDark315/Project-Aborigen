from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox, QListWidget, QListWidgetItem, QCheckBox, QVBoxLayout, QWidget, QHBoxLayout, QLabel
import sys
import json
import requests
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Responsive Window Size
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        MainWindow.resize(int(screen.width() * 0.8), int(screen.height() * 0.8))
        MainWindow.setMinimumSize(QtCore.QSize(1550, 820))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))

        # Main Widget
        self.main = QtWidgets.QWidget(MainWindow)
        self.main.setStyleSheet("background-color: #0E1621;")
        self.main.setObjectName("main")

        # Main Layout (Vertical)
        self.layout = QtWidgets.QVBoxLayout(self.main)

        # Search Layout (Horizontal)
        self.search_filter_layout = QtWidgets.QHBoxLayout()
        self.search_filter_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.search_filter_layout.setSpacing(50)

        # Search Bar
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setFixedSize(660, 75)
        font = QtGui.QFont()
        self.search_bar.setFont(font)
        self.search_bar.setStyleSheet("""QLineEdit{background-color: #454C55; color: #898989; border-radius: 35px; padding-left: 15px; font-size: 32px; border: 2px solid #626262;}
        QLineEdit:hover {border: 2px solid #898989;}""")
        self.search_bar.setPlaceholderText("Search for a game...")

        # Profile button
        self.profile_btn = AnimatedProfileButton("img/Profile.png")
        self.profile_btn.setFixedSize(100, 100)
        self.profile_btn.setIconSize(QtCore.QSize(75, 75))
        self.profile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profile_btn.setStyleSheet("""border: none;""")
        self.profile_btn.clicked.connect(self.open_profile)
        # Create Home Button
        self.home_btn = QtWidgets.QPushButton("Home")
        self.home_btn.setFixedSize(100, 50)
        self.home_btn.setFont(QtGui.QFont("Arial", 16))
        self.home_btn.setStyleSheet("""
            QPushButton {
                background-color: #454C55;
                color: white;
                border-radius: 20px;
                font-size: 16px;
                border: 2px solid #626262;
            }
            QPushButton:hover {
                background-color: #898989;
            }
        """)
        self.home_btn.clicked.connect(self.go_home)

        # Add Home Button to Layout (Top Left)
        self.search_filter_layout.addWidget(self.home_btn)



        # Add Home Button to Layout (Top Left)
        self.search_filter_layout.addWidget(self.home_btn)

        # Created by button
        self.created_by_btn = QtWidgets.QPushButton("Created by:")
        self.created_by_btn.setFixedSize(300, 75)
        self.profile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.created_by_btn.setStyleSheet("""QPushButton{background-color: #898989; color: #454C55; border: 2px solid #454C55; border-radius: 35px; font-size: 32px;}
        QPushButton:hover {border: 4px solid #454C55;}""")

        # Add Search Bar to Layout
        self.search_filter_layout.addWidget(self.created_by_btn)
        self.search_filter_layout.addWidget(self.search_bar)
        self.search_filter_layout.addWidget(self.profile_btn)

        # Grid Navigation Layout (Arrows + Game Grid)
        self.grid_navigation_layout = QtWidgets.QHBoxLayout()
        self.grid_navigation_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Left Arrow Button
        self.left_arrow = QtWidgets.QPushButton()
        self.left_arrow.setFixedSize(50, 50)
        self.left_arrow = AnimatedArrowButton("img/Arrow_Left.png")
        self.left_arrow.setIconSize(QtCore.QSize(40, 40))
        self.left_arrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_arrow.setStyleSheet("""QPushButton {background-color: transparent; border: none;}""")
        self.left_arrow.clicked.connect(self.prev_page)

        # Right Arrow Button
        self.right_arrow = QtWidgets.QPushButton()
        self.right_arrow.setFixedSize(50, 50)
        self.right_arrow = AnimatedArrowButton("img/Arrow_Right.png")
        self.right_arrow.setIconSize(QtCore.QSize(40, 40))
        self.right_arrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.right_arrow.setStyleSheet("""QPushButton {background-color: transparent; border: none;}""")
        self.right_arrow.clicked.connect(self.next_page)

        # Side Filter Layout
        self.main_layout = QtWidgets.QHBoxLayout(self.main)
        self.side_filter_layout = QtWidgets.QVBoxLayout()
        self.side_filter_widget = QtWidgets.QWidget()
        self.side_filter_widget.setLayout(self.side_filter_layout)
        self.side_filter_widget.setMaximumSize(320, 820)
        self.side_filter_widget.setMinimumSize(320, 700)
        self.side_filter_widget.setStyleSheet("background-color: transparent; margin-left: 25; margin-right: 25;")

        # Upload JSON file
        file_path = "data.json"
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Get developers and publishers
        publishers = set()
        developers = set()

        for game in data:
            pub_list = game.get("publisher", [])
            dev_list = game.get("developer", [])

            if isinstance(pub_list, str):
                pub_list = eval(pub_list) if pub_list.startswith("[") else [pub_list]
            if isinstance(dev_list, str):
                dev_list = eval(dev_list) if dev_list.startswith("[") else [dev_list]

            publishers.update(pub_list)
            developers.update(dev_list)

        publishers = sorted(publishers)
        developers = sorted(developers)

        # Header and item names for each list
        dropdown_titles = ["Publisher", "Developer", "Rating", "Price", "Platform", "Release Date", "Controller", "Age Rating", "Language"]

        predefined_options = {
            "Rating": ["From 60 to 69", "From 70 to 79", "From 80 to 89", "From 90 to 94", "From 95 to 100"],
            "Price": ["Free", "Under $10", "$10-$30", "$30-$60", "Above $60"],
            "Platform": ["Windows", "Mac", "Linux"],
            "Release Date": ["2024", "2023", "2022", "2010-2021", "Before 2010"],
            "Controller": ["Full Support", "No Support"],
            "Age Rating": ["0+", "8+", "12+", "13+", "14+", "15+", "16+", "17+"],
            "Language": ["English", "French", "German", "Italian", "Spanish - Spain", "Simplified Chinese", "Traditional Chinese", "Korean", "Russian", "Japanese", "Dutch", "Danish", "Finnish", "Norwegian", "Polish", "Portuguese - Portugal", "Swedish", "Thai", "Turkish"]
        }

        # Dropdown lists
        for i, title in enumerate(dropdown_titles):
            dropdown = QtWidgets.QComboBox()
            dropdown.addItem(f"All {title}")  # Add "All" option

            if title == "Publisher":
                publishers = [pub for pub in publishers if pub.strip()]
                dropdown.addItems(publishers)
            elif title == "Developer":
                developers = [dev for dev in developers if dev.strip()]
                dropdown.addItems(developers)
            else:
                dropdown.addItems(predefined_options.get(title, []))

            dropdown.setStyleSheet(""" QComboBox {background-color: #454C55; border: none; height: 50px;
                                    border-radius: 25px; padding-left: 30px; font-size: 28px; color: #000; }
                                    QComboBox::drop-down {background-color: transparent; }
                                    QComboBox QAbstractItemView {font-size: 20px; background-color: #454C55;
                                    color: #000; selection-background-color: #454C55; selection-color: #898989;
                                    border-radius: 10px; outline: none;}""")

            # **Connect each filter to perform_search**
            dropdown.currentIndexChanged.connect(self.perform_search)

            # Store filters in a list for easy access
            setattr(self, f"{title.lower().replace(' ', '_')}_filter", dropdown)

            self.side_filter_layout.addWidget(dropdown)



        # Grid Layout for Displaying Games
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setSpacing(20)
        self.grid_widget = QtWidgets.QWidget()
        self.grid_widget.setLayout(self.grid_layout)
        self.grid_widget.setVisible(False)

        # Add to Grid Navigation Layout
        self.grid_navigation_layout.addWidget(self.side_filter_widget)
        self.grid_navigation_layout.addWidget(self.left_arrow)
        self.grid_navigation_layout.addWidget(self.grid_widget)
        self.grid_navigation_layout.addWidget(self.right_arrow)

        # Add to Main Layout
        self.layout.addLayout(self.search_filter_layout)
        self.layout.addLayout(self.grid_navigation_layout)

        MainWindow.setCentralWidget(self.main)

        # Load Game Data
        self.games_data, self.games_data_dict = self.load_game_data("data.json")
        self.current_page = 0

        # Connect search bar & filter event
        self.search_timer = QtCore.QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.perform_search)
        self.search_bar.textChanged.connect(self.delayed_search)

        # Show all games initially
        self.perform_search()

    def go_home(self):
                """Switch the source back to data.json and update the UI."""
                print("🏠 Home button clicked: Showing all games.")

                # Switch back to all games (load from data.json)
                self.perform_search("data.json")


    def load_game_data(self, file_path):
        """Load game data from the specified JSON file."""
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    games = json.load(file)

                # ✅ Handle `favorites.json` (stored as a dictionary)
                if isinstance(games, dict):
                    games_list = list(games.values())  # Convert dictionary to list
                else:
                    games_list = games  # Already a list

                # Convert list to dictionary for quick lookup
                games_dict = {str(game["appid"]): game for game in games_list}

                return games_list, games_dict

            except json.JSONDecodeError:
                print(f"⚠️ Error: {file_path} is corrupted. Returning empty list.")
                return [], {}

        else:
            print(f"⚠️ Warning: {file_path} not found. Returning empty list.")
            return [], {}


    def delayed_search(self):
        self.search_timer.start(500)

        # ✅ Sort games by rating (Highest to Lowest)
        def get_valid_rating(game):
            rating = str(game.get("rating", "0"))
            return int(rating) if rating.isdigit() else 0

        self.filtered_games.sort(key=get_valid_rating, reverse=True)

        # ✅ Print how many games were found (Debugging)
        print(f"🔍 Found {len(self.filtered_games)} games after filtering.")

        # ✅ Reset to first page whenever search updates
        self.current_page = 0

        # ✅ Show/hide grid based on results
        self.grid_widget.setVisible(len(self.filtered_games) > 0)

        # ✅ Display games
        self.display_game_icons()

    def perform_search(self, data_source="data.json"):
        """Update game results dynamically from the specified data source."""

        # ✅ If switching back to all games, reset `is_profile_mode`
        if data_source == "data.json":
            self.is_profile_mode = False

        # Load data from the given source file
        self.games_data, self.games_data_dict = self.load_game_data(data_source)

        search_query = self.search_bar.text().strip().lower()

        # Filter games normally
        self.filtered_games = list(filter(lambda game: search_query in game["name"].lower(), self.games_data))

        # ✅ Sort games by rating (Highest to Lowest)
        def get_valid_rating(game):
            rating = str(game.get("rating", "0"))
            return int(rating) if rating.isdigit() else 0

        self.filtered_games.sort(key=get_valid_rating, reverse=True)

        print(f"🔍 Found {len(self.filtered_games)} games from {data_source}.")

        self.current_page = 0  # Reset page index

        self.grid_widget.setVisible(len(self.filtered_games) > 0)
        self.display_game_icons()



    def display_game_icons(self):
        while self.grid_layout.count():
            widget = self.grid_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        total_games = len(self.filtered_games)
        start_index = self.current_page * 6
        end_index = start_index + 6
        games_to_display = self.filtered_games[start_index:end_index]

        # ✅ Print which games are being displayed (Debugging)
        print(f"📄 Showing games {start_index + 1} to {end_index} out of {total_games}")

        row, col = 0, 0
        for game in games_to_display:
            print(f"🎮 Adding game: {game['name']}")
            game_widget = self.create_game_card(game)
            self.grid_layout.addWidget(game_widget, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # ✅ Enable/Disable Arrows based on pages
        self.left_arrow.setEnabled(self.current_page > 0)
        self.right_arrow.setEnabled((self.current_page + 1) * 6 < len(self.filtered_games))

    def next_page(self):
        if (self.current_page + 1) * 6 < len(self.filtered_games):
            self.current_page += 1
            self.display_game_icons()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_game_icons()

    def create_game_card(self, game):
        game_card = QtWidgets.QFrame()
        game_card.setFixedSize(350, 300)
        game_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        game_card.setStyleSheet("""QFrame{border-radius: 35px; background-color: #454C55;}""")

        main_layout = QtWidgets.QVBoxLayout(game_card)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 🖼️ Game Image (Using QPixmap)
        game_img = QtWidgets.QLabel()
        game_img.setFixedSize(350, 180)

        game_pixmap = self.download_image(game["img"])
        if game_pixmap:
            game_img.setPixmap(game_pixmap)
            game_img.setScaledContents(True)

        main_layout.addWidget(game_img)

        # Game Name Layout
        info_layout = QtWidgets.QHBoxLayout()
        info_layout.setContentsMargins(15, 5, 15, 0)
        truncated_name = self.truncate_text(game["name"], 25)
        game_name = QtWidgets.QLabel(truncated_name)
        game_name.setStyleSheet("font-size: 22px; color: #fff;")
        info_layout.addWidget(game_name)
        info_layout.addStretch()

        main_layout.addLayout(info_layout)

        # ⭐ Rating & Controller Layout
        rating_layout = QtWidgets.QHBoxLayout()
        rating_layout.setContentsMargins(15, 5, 15, 10)

        rating = game.get("rating", "N/A")
        metacritic_icon = QtWidgets.QLabel()
        metacritic_pixmap = QtGui.QPixmap("img/Metacritic_Logo.png").scaled(30, 30, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        metacritic_icon.setPixmap(metacritic_pixmap)

        rating_label = QtWidgets.QLabel(f"{rating}")
        rating_label.setStyleSheet("font-size: 20px; color: #fff;")

        rating_layout.addWidget(metacritic_icon)
        rating_layout.addWidget(rating_label)
        rating_layout.addStretch()

        # 🎮 Controller Icon
        controller_icon = QtWidgets.QLabel()
        controller_img = "img/Controller_On.png" if game.get("controller_support") == "full" else "img/Controller_Off.png"
        controller_pixmap = QtGui.QPixmap(controller_img).scaled(30, 30, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        controller_icon.setPixmap(controller_pixmap)
        rating_layout.addWidget(controller_icon)
        rating_layout.addSpacing(10)

        # ⭐ Bookmark Button (Add to Favorites)
        bookmark_button = QtWidgets.QPushButton()
        bookmark_button.setFixedSize(40, 40)
        bookmark_button.setStyleSheet("background: transparent; border: none;")

        # Set default bookmark state
        favorites = self.load_favorites()
        if game["appid"] in favorites:
            bookmark_button.setIcon(QtGui.QIcon("img/Bookmark_Fill.png"))
        else:
            bookmark_button.setIcon(QtGui.QIcon("img/Bookmark_No_Fill.png"))

        bookmark_button.clicked.connect(lambda: self.toggle_favorite(game, bookmark_button))

        rating_layout.addWidget(bookmark_button)

        main_layout.addLayout(rating_layout)

        return game_card


    def toggle_favorite(self, game, button):
        """Toggle a game in the favorites list (add/remove)."""
        favorites = self.load_favorites()
        game_id = str(game["appid"])  # Ensure game IDs are strings

        if game_id in favorites:
            del favorites[game_id]  # Remove game
            button.setIcon(QtGui.QIcon("img/Bookmark_No_Fill.png"))  # Change to unfilled icon
            print(f"❌ Removed {game['name']} from favorites.")
        else:
            favorites[game_id] = game  # Add game
            button.setIcon(QtGui.QIcon("img/Bookmark_Fill.png"))  # Change to filled icon
            print(f"⭐ Added {game['name']} to favorites.")

        self.save_favorites(favorites)



    def load_favorites(self):
        """Load favorite games from a JSON file (returns a dictionary)."""
        if os.path.exists("favorites.json"):
            try:
                with open("favorites.json", "r", encoding="utf-8") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}  # Return empty if file is corrupted
        return {}

    def save_favorites(self, favorites):
        """Save favorite games to JSON file."""
        with open("favorites.json", "w", encoding="utf-8") as file:
            json.dump(favorites, file, indent=4, ensure_ascii=False)


    def hide_widgets_in_layout(self, layout):
        """Hide all widgets in the given layout."""
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setVisible(False)

    def show_widgets_in_layout(self, layout):
        """Show all widgets in the given layout."""
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setVisible(True)

    def open_profile(self):
        """Update the game display to show only favorite games without hiding filters/search bar."""

        # ✅ Change data source to `favorites.json`
        self.perform_search("favorites.json")

        # ✅ Keep all UI elements visible (DO NOT hide filters, search bar, or arrows)
        self.show_widgets_in_layout(self.search_filter_layout)
        self.show_widgets_in_layout(self.grid_navigation_layout)

        print("🔹 Switched to profile mode. Showing only favorite games.")





    def remove_from_favorites(self, game):
        """Remove a game from favorites and refresh the UI to show updated favorites."""
        favorites = self.load_favorites()

        game_id = str(game["appid"])

        if game_id in favorites:
            del favorites[game_id]
            self.save_favorites(favorites)
            print(f"❌ Removed {game['name']} from favorites.")

        self.open_profile()  # Refresh the profile section in the same window



    def truncate_text(self, text, max_length):
        return text if len(text) <= max_length else text[:max_length] + "..."

    def download_image(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            image = QtGui.QImage()
            image.loadFromData(response.content)
            return QtGui.QPixmap(image)
        except Exception as e:
            print(f"Failed to load image: {url} - {e}")
            return None


class AnimatedArrowButton(QtWidgets.QPushButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setIcon(QtGui.QIcon(icon_path))
        self.setIconSize(QtCore.QSize(40, 40))

        # Transparency effect for inactive state
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)

        # Resize Animation
        self.animation = QtCore.QPropertyAnimation(self, b"iconSize")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

        self.original_size = QtCore.QSize(40, 40)
        self.hover_size = QtCore.QSize(50, 50)
        self.disabled_size = QtCore.QSize(30, 30)
        self.is_hover_enabled = True

    def setEnabled(self, enabled):
        super().setEnabled(enabled)
        self.is_hover_enabled = enabled

        if enabled:
            self.opacity_effect.setOpacity(1.0)
            self.setIconSize(self.original_size)
        else:
            self.opacity_effect.setOpacity(0.4)
            self.setIconSize(self.disabled_size)

    def enterEvent(self, event):
        if self.is_hover_enabled:
            self.animation.stop()
            self.animation.setStartValue(self.original_size)
            self.animation.setEndValue(self.hover_size)
            self.animation.start()

    def leaveEvent(self, event):
        if self.is_hover_enabled:
            self.animation.stop()
            self.animation.setStartValue(self.hover_size)
            self.animation.setEndValue(self.original_size)
            self.animation.start()

class AnimatedProfileButton(QtWidgets.QPushButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        self.setIcon(QtGui.QIcon(icon_path))

        # Анимация изменения размера
        self.animation = QtCore.QPropertyAnimation(self, b"iconSize")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

        self.original_size = QtCore.QSize(75, 75)
        self.hover_size = QtCore.QSize(85, 85)
        self.is_hover_enabled = True

    def enterEvent(self, event):
        if self.is_hover_enabled:
            self.animation.stop()
            self.animation.setStartValue(self.original_size)
            self.animation.setEndValue(self.hover_size)
            self.animation.start()

    def leaveEvent(self, event):
        if self.is_hover_enabled:
            self.animation.stop()
            self.animation.setStartValue(self.hover_size)
            self.animation.setEndValue(self.original_size)
            self.animation.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
