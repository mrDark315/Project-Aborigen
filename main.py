from PyQt5 import QtWidgets
import sys
from pages.HomePage import HomePage

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Основной контейнер для страниц
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Словарь страниц
        self.pages = {}

        # Загружаем страницы
        self.load_page("home", HomePage(self))

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
