from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
import sys
from pages.HomePage import HomePage
from pages.ProfilePage import ProfilePage
# from pages.GameCardPage import GameCardPage
# from pages.CreatedByPage import CreatedByPage

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Responsive Window Size
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        self.resize(int(screen.width() * 0.8), int(screen.height() * 0.8))
        self.setMinimumSize(QSize(1600, 970))
        self.setMaximumSize(QSize(1920, 1080))

        # Основной контейнер для страниц
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Словарь страниц
        self.pages = {}

        # Загружаем страницы
        self.load_page("home", HomePage(self))
        self.load_page("profile", ProfilePage(self))
        # self.load_page("game_card", GameCardPage(self))
        # self.load_page("created_by", CreatedByPage(self))

        # Устанавливаем страницу по умолчанию
        self.set_page("home")

    def load_page(self, name, page):
        self.pages[name] = page
        self.central_widget.addWidget(page)

    def set_page(self, name):
        if name in self.pages:
            self.central_widget.setCurrentWidget(self.pages[name])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
