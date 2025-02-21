from PyQt5 import QtWidgets, QtGui, QtCore

class CreatedByButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, text="Created by:"):
        super().__init__(text, parent if isinstance(parent, QtWidgets.QWidget) else None)

        self.setFixedSize(275, 75)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("""QPushButton {background-color: #898989; color: #454C55; border: 2px solid #454C55; border-radius: 35px; font-size: 32px;} QPushButton:hover {border: 4px solid #454C55;}""")
