from PyQt5 import QtWidgets, QtGui, QtCore
import requests

class GameCardHome(QtWidgets.QFrame):
    def __init__(self, game, parent_ui):
        super().__init__(parent_ui.main)
        self.game = game
        self.parent_ui = parent_ui

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
        rating = game.get("rating", "N/A")
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

        # ⭐ Bookmark Button
        bookmark_button = QtWidgets.QPushButton()
        bookmark_button.setIconSize(QtCore.QSize(40, 40))
        bookmark_button.setFixedSize(30, 40)
        bookmark_button.setStyleSheet("background: transparent; border: none;")
        bookmark_button.setIcon(QtGui.QIcon("img/Bookmark_No_Fill.png"))

        rating_layout.addWidget(bookmark_button)
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
