from PyQt5 import QtWidgets, QtGui, QtCore
from func.display_profile_games import display_profile_games
import requests, json

class GameCardHome(QtWidgets.QFrame):
    def __init__(self, game, parent_ui):
        super().__init__(parent_ui)
        self.game = game
        self.parent_ui = parent_ui
        self.game_id = str(game.get("id", "Unknown"))

        self.setMaximumSize(460, 400)
        self.setMinimumSize(360, 300)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("QFrame{border-radius: 35px; background-color: #454C55;}")

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Game Image
        game_img = QtWidgets.QLabel()
        game_img.setMaximumSize(460, 215)
        game_img.setMinimumSize(360, 215)

        game_pixmap = self.download_image(game.get("img", ""))
        if game_pixmap:
            game_img.setPixmap(game_pixmap)
            game_img.setScaledContents(True)

        main_layout.addWidget(game_img)

        # Game Name
        info_layout = QtWidgets.QHBoxLayout()
        info_layout.setContentsMargins(20, 5, 20, 0)
        truncated_name = self.truncate_text(game.get("name", "Unknown Game"), 32)
        game_name = QtWidgets.QLabel(truncated_name)
        game_name.setStyleSheet("font-size: 24px; color: #fff;")
        info_layout.addWidget(game_name)
        info_layout.addStretch()

        main_layout.addLayout(info_layout)

        # Rating & Controller
        rating_layout = QtWidgets.QHBoxLayout()
        rating_layout.setContentsMargins(20, 5, 20, 15)

        # Metacritic rating
        rating = game.get("metacritic_score", "N/A")
        metacritic_icon = QtWidgets.QLabel()
        metacritic_pixmap = QtGui.QPixmap("img/Metacritic_Logo.png").scaled(40, 40, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        metacritic_icon.setPixmap(metacritic_pixmap)

        rating_label = QtWidgets.QLabel(f"{rating}")
        rating_label.setStyleSheet("font-size: 20px; color: #fff;")

        rating_layout.addWidget(metacritic_icon)
        rating_layout.addWidget(rating_label)
        rating_layout.addStretch()

        # Controller Icon
        controller_icon = QtWidgets.QLabel()
        controller_img = "img/Controller_On.png" if game.get("controller_support", "").lower() == "full" else "img/Controller_Off.png"
        controller_pixmap = QtGui.QPixmap(controller_img).scaled(40, 30, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        controller_icon.setPixmap(controller_pixmap)
        rating_layout.addWidget(controller_icon)
        rating_layout.addSpacing(10)

        # Bookmark Button
        self.bookmark_button = QtWidgets.QPushButton()
        self.bookmark_button.setIconSize(QtCore.QSize(40, 40))
        self.bookmark_button.setFixedSize(30, 40)
        self.bookmark_button.setStyleSheet("background: transparent; border: none;")
        self.bookmark_button.clicked.connect(self.toggle_favorite)
        self.update_bookmark_icon()

        rating_layout.addWidget(self.bookmark_button)
        main_layout.addLayout(rating_layout)

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

    def truncate_text(self, text, max_length):
        return text if len(text) <= max_length else text[:max_length] + "..."

    def toggle_favorite(self):
        saved_games = self.load_saved_games()
        game_info = {
            "id": str(self.game.get("id", "Unknown")),
            "name": self.game.get("name", "Unknown Game"),
            "img": self.game.get("img", "")
        }

        existing_game = next((g for g in saved_games if isinstance(g, dict) and g.get("id") == game_info["id"]), None)

        if existing_game:
            saved_games.remove(existing_game)
            print(f"❌ Removed from favorites: {game_info['name']}")
        else:
            saved_games.append(game_info)
            print(f"✅ Added to favorites: {game_info['name']}")

        self.save_saved_games(saved_games)
        self.update_bookmark_icon()
        main_window = self.find_main_window()

        # If the profile page is displayed, refresh it
        if main_window and "profile" in main_window.pages:
            display_profile_games(main_window.pages["profile"])

    def find_main_window(self):
        parent = self.parent_ui
        while parent is not None:
            if isinstance(parent, QtWidgets.QMainWindow):
                return parent
            parent = parent.parent
        return None

    def update_bookmark_icon(self):
        saved_games = self.load_saved_games()
        icon = "img/Bookmark_Fill.png" if any(g["id"] == self.game_id for g in saved_games) else "img/Bookmark_No_Fill.png"
        self.bookmark_button.setIcon(QtGui.QIcon(icon))

    @staticmethod
    def load_saved_games():
        try:
            with open("store/saved_games.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                return [g for g in data if isinstance(g, dict)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def save_saved_games(saved_games):
        with open("store/saved_games.json", "w", encoding="utf-8") as file:
            json.dump(saved_games, file, indent=4, ensure_ascii=False)
