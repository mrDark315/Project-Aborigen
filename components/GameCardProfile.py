from PyQt5 import QtWidgets, QtGui, QtCore
import requests

class GameCardProfile(QtWidgets.QFrame):
    def __init__(self, game, parent_ui):
        super().__init__(parent_ui)
        self.game = game
        self.parent_ui = parent_ui

        self.setMaximumSize(460, 400)
        self.setMinimumSize(360, 300)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("QFrame{border-radius: 35px; background-color: #343a40;}")

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        game_img = QtWidgets.QLabel()
        game_img.setMaximumSize(460, 215)
        game_img.setMinimumSize(360, 215)
        game_pixmap = self.download_image(game.get("img", ""))
        if game_pixmap:
            game_img.setPixmap(game_pixmap)
            game_img.setScaledContents(True)
        main_layout.addWidget(game_img)

        game_name = QtWidgets.QLabel(game.get("name", "Unknown Game"))
        game_name.setStyleSheet("font-size: 22px; color: #ffcc00; font-weight: bold;")
        game_name.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(game_name)

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
