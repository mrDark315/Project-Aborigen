from PyQt5 import QtWidgets, QtGui, QtCore
import os

class AnimatedCloseButton(QtWidgets.QPushButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)

        if isinstance(icon_path, str) and os.path.exists(icon_path):
            self.setIcon(QtGui.QIcon(icon_path))
        else:
            print(f"⚠️ Error: icon file {icon_path} not found!")

        # Hover resize animation
        self.animation = QtCore.QPropertyAnimation(self, b"iconSize")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

        self.original_size = QtCore.QSize(50, 50)
        self.hover_size = QtCore.QSize(55, 55)
        self.is_hover_enabled = True

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

class CloseButton(AnimatedCloseButton):
    def __init__(self, parent, icon_path="img/Cross.png"):
        super().__init__(icon_path, parent)

        # Search for `MainWindow`
        self.main_window = self.find_main_window(parent)

        self.setFixedSize(55, 55)
        self.setIconSize(QtCore.QSize(50, 50))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("border: none; background: transparent;")

        self.clicked.connect(self.go_to_home)

    def find_main_window(self, widget):
        while widget is not None:
            if isinstance(widget, QtWidgets.QMainWindow):
                return widget
            widget = widget.parent()
        return None

    def go_to_home(self):
        if self.main_window:
            print("🔄 Close ProfilePage")
            self.main_window.set_page("home")
        else:
            print("⚠️ Error: MainWindow not found!")
