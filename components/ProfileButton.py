from PyQt5 import QtWidgets, QtGui, QtCore

class AnimatedProfileButton(QtWidgets.QPushButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        self.setIcon(QtGui.QIcon(icon_path))

        # Resize Animation
        self.animation = QtCore.QPropertyAnimation(self, b"iconSize")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

        self.original_size = QtCore.QSize(75, 75)
        self.hover_size = QtCore.QSize(85, 85)
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

class ProfileButton(AnimatedProfileButton):
    def __init__(self, main_window, icon_path="img/Profile.png"):
        super().__init__(icon_path, main_window)
        self.main_window  = main_window
        self.setIcon(QtGui.QIcon(icon_path))

        self.setFixedSize(100, 100)
        self.setIconSize(QtCore.QSize(75, 75))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("border: none;")

        self.clicked.connect(self.open_profile)

    def open_profile(self):
        print("🔄 Open Profile Page")
        self.main_window.set_page("profile")