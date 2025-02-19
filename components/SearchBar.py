from PyQt5 import QtWidgets, QtGui, QtCore
from func.search_func import handle_search, delay_search

class SearchBar(QtWidgets.QLineEdit):
    def __init__(self, parent_ui):
        super().__init__()
        self.parent_ui = parent_ui

        self.setFixedSize(700, 75)
        font = QtGui.QFont()
        self.setFont(font)
        self.setStyleSheet("""QLineEdit{background-color: #454C55; color: #898989; border-radius: 35px; padding-left: 15px; font-size: 32px; border: 2px solid #626262;}
            QLineEdit:hover {border: 2px solid #898989;}""")
        self.setPlaceholderText("Enter at least 3 letters to search games...")

        self.search_timer = QtCore.QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(lambda: handle_search(self.parent_ui))
        self.textChanged.connect(lambda: delay_search(self.parent_ui))
