from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
import os, sys, json, requests
from func.download_data import cached_games_data
from func.nav_pages import next_page, prev_page
from func.search_func import handle_search, delay_search
from components.SearchBar import SearchBar
from components.ProfileButton import ProfileButton
from components.CreatedByButton import CreatedByButton
from components.NavArrows import AnimatedArrowButton

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

        # Search Bar
        self.search_bar = SearchBar(self)

        # Profile button
        self.profile_btn = ProfileButton(self)

        # Create Home Button
        # self.home_btn = QtWidgets.QPushButton("Home")
        # self.home_btn.setFixedSize(100, 50)
        # self.home_btn.setFont(QtGui.QFont("Arial", 16))
        # self.home_btn.setStyleSheet("""QPushButton {background-color: #454C55; color: white; border-radius: 20px; font-size: 16px; border: 2px solid #626262;}
        #     QPushButton:hover {background-color: #898989;}""")
        # self.home_btn.clicked.connect(self.go_home)

        # Add Home Button to Layout (Top Left)
        # self.search_filter_layout.addWidget(self.home_btn)

        # Created by button
        self.created_by_btn = CreatedByButton(self)

        # Add Search Bar to Layout
        self.search_filter_layout.addWidget(self.created_by_btn)
        self.search_filter_layout.addWidget(self.search_bar)
        self.search_filter_layout.addWidget(self.profile_btn)

        # Grid Navigation Layout (Arrows + Game Grid)
        self.grid_navigation_layout = QtWidgets.QHBoxLayout()
        self.grid_navigation_layout.setAlignment(Qt.AlignCenter)

        # Left Arrow Button
        self.left_arrow = AnimatedArrowButton("img/Arrow_Left.png")
        self.left_arrow.clicked.connect(lambda: prev_page(self))

        # Right Arrow Button
        self.right_arrow = AnimatedArrowButton("img/Arrow_Right.png")
        self.right_arrow.clicked.connect(lambda: next_page(self))

        # Side Filter Layout
        self.main_layout = QtWidgets.QHBoxLayout(self.main)
        self.side_filter_layout = QtWidgets.QVBoxLayout()
        self.side_filter_widget = QtWidgets.QWidget()
        self.side_filter_widget.setLayout(self.side_filter_layout)
        self.side_filter_widget.setMaximumSize(320, 820)
        self.side_filter_widget.setMinimumSize(320, 700)
        self.side_filter_widget.setStyleSheet("background-color: transparent; margin-left: 25;")

        # Upload JSON file
        file_path = "store/data.json"
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

        dropdown_titles = ["Publisher", "Developer", "Rating", "Price", "Release Date" , "Age Rating", "Language","Platform", "Controller"]

        predefined_options = {
            "Rating": ["From 60 to 69", "From 70 to 79", "From 80 to 89", "From 90 to 94", "From 95 to 100"],
            "Price": ["Free", "Under $10", "$10-$30", "$30-$60", "Above $60"],
            "Platform": ["Windows", "Mac", "Linux"],
            "Age Rating": ["0+", "8+", "12+", "13+", "14+", "15+", "16+", "17+"],
            "Language": ["English", "French", "German", "Italian", "Spanish - Spain", "Simplified Chinese", "Traditional Chinese", "Korean", "Russian", "Japanese", "Dutch", "Danish", "Finnish", "Norwegian", "Polish", "Portuguese - Portugal", "Swedish", "Thai", "Turkish"],
            "Release Date": ["2024", "2023", "2022", "2010-2021", "Before 2010"],
            "Controller": ["Full Support", "No Support"]
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

            dropdown.setStyleSheet(""" QComboBox {background-color: #454C55; border: none; height: 50px; border-radius: 25px; padding-left: 30px; font-size: 28px; color: #000;} QComboBox::drop-down {background-color: transparent;}
            QComboBox QAbstractItemView {font-size: 20px; background-color: #454C55; color: #000; selection-background-color: #454C55; selection-color: #898989; border-radius: 10px; outline: none;}""")

            # Connect each filter to perform_search
            dropdown.currentIndexChanged.connect(lambda: handle_search(self))

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
        self.filtered_games = cached_games_data[:]
        self.current_page = 0
        handle_search(self)


        # Connect search bar & filter event
        self.search_timer = QtCore.QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(lambda: handle_search(self))
        self.search_bar.textChanged.connect(lambda: delay_search(self))

    def go_home(self):
                print("🏠 Home button clicked: Showing all games.")
                handle_search(self)

    def display_game_icons(self):
        while self.grid_layout.count():
            widget = self.grid_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        total_games = len(self.filtered_games)
        start_index = self.current_page * 6
        end_index = min(start_index + 6, total_games)
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
        self.right_arrow.setEnabled((self.current_page + 1) * 6 < total_games)

    def create_game_card(self, game):
        game_card = QtWidgets.QFrame()
        game_card.setMaximumSize(460, 400)
        game_card.setMinimumSize(360, 300)
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
        if os.path.exists("store/favorites.json"):
            try:
                with open("store/favorites.json", "r", encoding="utf-8") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}  # Return empty if file is corrupted
        return {}

    def save_favorites(self, favorites):
        """Save favorite games to JSON file."""
        with open("store/favorites.json", "w", encoding="utf-8") as file:
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
        self.perform_search("store/favorites.json")

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
