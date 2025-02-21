from PyQt5 import QtWidgets, QtGui, QtCore

class SortingButtons(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(400, 0, 60, 0)
        self.layout.setSpacing(65)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        button_texts = ["All Games", "Favorite", "Completed"]

        self.buttons = []
        for i, text in enumerate(button_texts):
            if i > 0:
                spacer = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.layout.addItem(spacer)

            button = QtWidgets.QPushButton(text)
            button.setFixedSize(400, 70)
            button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            button.setStyleSheet("""QPushButton {background-color: #454C55; color: #000; font-size: 28px; border: none; border-radius: 35px; padding: 10px;} QPushButton:hover {background-color: #898989;}""")
            self.layout.addWidget(button)
            self.buttons.append(button)

        self.layout.addStretch()

    def get_buttons(self):
        return self.buttons
