from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

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
        QLineEdit:focus {border: 2px solid #898989;}""")
        self.search_bar.setPlaceholderText("Search for a game...")

        # Profile button
        self.profile_btn = QtWidgets.QPushButton()
        self.profile_btn.setFixedSize(75, 75)
        self.profile_btn.setIcon(QtGui.QIcon("img/Profile.png"))
        self.profile_btn.setIconSize(QtCore.QSize(75, 75))
        self.profile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profile_btn.setStyleSheet("""background-color: transparent; border: none;}""")

        # Created by button
        self.created_by_btn = QtWidgets.QPushButton("Created by:")
        self.created_by_btn.setFixedSize(300, 75)
        self.profile_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.created_by_btn.setStyleSheet("""QPushButton{background-color: #898989; color: #454C55; border: 2px solid #454C55; border-radius: 35px; font-size: 32px;}
        QPushButton:hover {border: 4px solid #454C55;}""")

        # Add Search Bar & Filter to Layout
        self.search_filter_layout.addWidget(self.created_by_btn)
        self.search_filter_layout.addWidget(self.search_bar)
        self.search_filter_layout.addWidget(self.profile_btn)

        # Grid Navigation Layout (Arrows + Game Grid)
        self.grid_navigation_layout = QtWidgets.QHBoxLayout()
        self.grid_navigation_layout.setAlignment(QtCore.Qt.AlignCenter)

        # ⬅ Left Arrow Button (Using Image)
        self.left_arrow = QtWidgets.QPushButton()
        self.left_arrow.setFixedSize(50, 50)
        self.left_arrow = Animated_Arrow_Button("img/Arrow_Left.png")
        self.left_arrow.setIconSize(QtCore.QSize(40, 40))
        self.left_arrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_arrow.setStyleSheet("""QPushButton {background-color: transparent; border: none;}""")
        self.left_arrow.clicked.connect(self.prev_page)

        # ➡ Right Arrow Button (Using Image)
        self.right_arrow = QtWidgets.QPushButton()
        self.right_arrow.setFixedSize(50, 50)
        self.right_arrow = Animated_Arrow_Button("img/Arrow_Right.png")
        self.right_arrow.setIconSize(QtCore.QSize(40, 40))
        self.right_arrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.right_arrow.setStyleSheet("""QPushButton {background-color: transparent; border: none;}""")
        self.right_arrow.clicked.connect(self.next_page)

        # Grid Layout for Displaying Games
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setSpacing(20)
        self.grid_widget = QtWidgets.QWidget()
        self.grid_widget.setLayout(self.grid_layout)
        self.grid_widget.setVisible(False)

        # Add to Grid Navigation Layout
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

    def load_game_data(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                games_list = json.load(file)

            # Создаем словарь для быстрого доступа по названию
            games_dict = {game["name"].lower(): game for game in games_list}

            return games_list, games_dict

        except Exception as e:
            print(f"Error loading data.json: {e}")
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

    def perform_search(self):
        search_query = self.search_bar.text().strip().lower()

        # Фильтрация без создания нового списка (используем filter)
        self.filtered_games = list(filter(lambda game: search_query in game["name"].lower(), self.games_data))

        # Преобразование строки рейтинга в число для сравнения
        def get_valid_rating(game):
            rating = str(game.get("rating", "0"))
            return int(rating) if rating.isdigit() else 0

        # Проверяем, была ли сортировка уже выполнена
        if not hasattr(self, "_is_sorted") or not self._is_sorted:
            self.filtered_games.sort(key=get_valid_rating, reverse=True)
            self._is_sorted = True  # Отмечаем, что сортировка уже была

        print(f"🔍 Найдено {len(self.filtered_games)} игр после фильтрации.")

        self.current_page = 0  # Сбрасываем страницу

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
        game_card.setFixedSize(460, 350)
        game_card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        game_card.setStyleSheet("""QFrame{border-radius: 35px; background-color: #454C55;}""")

        main_layout = QtWidgets.QVBoxLayout(game_card)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 🖼️ Game Image (Using QPixmap + mask)
        game_img = QtWidgets.QLabel()
        game_img.setGeometry(QtCore.QRect(0, 0, 460, 215))

        game_pixmap = self.download_image(game["img"])
        if game_pixmap:
            game_img.setPixmap(game_pixmap)
            game_img.setScaledContents(True)

            # Apply mask to round the top corners
            mask = QtGui.QRegion(game_img.rect())
            radius = 35

            left_circle_region = QtGui.QRegion(0, 0, radius*2, radius*2, QtGui.QRegion.Ellipse)
            right_circle_region = QtGui.QRegion(game_img.width() - radius*2, 0, radius*2, radius*2, QtGui.QRegion.Ellipse)

            final_mask = mask.intersected(left_circle_region.united(right_circle_region).boundingRect())

            mask = QtGui.QRegion(game_img.rect())
            mask -= QtGui.QRegion(0, 0, radius, radius)
            mask -= QtGui.QRegion(game_img.width() - radius, 0, radius, radius)

            left_circle_region = QtGui.QRegion(0, 0, radius*2, radius*2, QtGui.QRegion.Ellipse)
            right_circle_region = QtGui.QRegion(game_img.width() - radius*2, 0, radius*2, radius*2, QtGui.QRegion.Ellipse)
            final_mask = mask.united(left_circle_region).united(right_circle_region)

            game_img.setMask(final_mask)

        main_layout.addWidget(game_img)

        # Game Name & Platform Layout
        info_layout = QtWidgets.QHBoxLayout()
        info_layout.setContentsMargins(20, 10, 20, 0)
        truncated_name = self.truncate_text(game["name"], 29)
        game_name = QtWidgets.QLabel(truncated_name)
        game_name.setStyleSheet("font-size: 30px; color: #fff;")
        info_layout.addWidget(game_name)

        info_layout.addStretch()
        main_layout.addLayout(info_layout)

        # Rating & Controller Layout
        rating_layout = QtWidgets.QHBoxLayout()
        rating_layout.setContentsMargins(20, 10, 20, 20)

        try:
            metacritic_data = eval(game.get("metacritic", "{}"))
            rating = metacritic_data.get("score", "N/A")
        except Exception:
            rating = "N/A"

        # Create QLabel for logo
        metacritic_icon = QtWidgets.QLabel()
        metacritic_pixmap = QtGui.QPixmap("img/Metacritic_Logo.png")
        metacritic_pixmap = metacritic_pixmap.scaled(40, 40, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        metacritic_icon.setPixmap(metacritic_pixmap)

        # Create QLabel for rating
        rating_label = QtWidgets.QLabel(f"{rating}")
        rating_label.setStyleSheet("font-size: 28px; color: #fff;")

        # Add icon&rating in `rating_layout`
        rating_layout.addWidget(metacritic_icon)
        rating_layout.addWidget(rating_label)
        rating_layout.addWidget(rating_label)
        rating_layout.addStretch()

        # 🎮 Controller Icon
        controller_icon = QtWidgets.QLabel()
        controller_img = "img/Controller_On.png" if game.get("controller_support") == "full" else "img/Controller_Off.png"
        controller_pixmap = QtGui.QPixmap(controller_img)
        controller_icon.setPixmap(controller_pixmap.scaled(40, 33, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        rating_layout.addWidget(controller_icon)
        rating_layout.addSpacing(20)

        # Bookmark Icon
        bookmark_label = QtWidgets.QLabel()
        star_pixmap = QtGui.QPixmap("img/Bookmark_No_Fill.png")
        bookmark_label.setPixmap(star_pixmap.scaled(40, 40, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        rating_layout.addWidget(bookmark_label)

        main_layout.addLayout(rating_layout)

        return game_card

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


class Animated_Arrow_Button(QtWidgets.QPushButton):
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
