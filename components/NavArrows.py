from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from func.nav_pages import next_page, prev_page

class AnimatedArrowButton(QtWidgets.QPushButton):
    def __init__(self, icon_path, parent_ui, direction):
        super().__init__(parent_ui)
        self.parent_ui = parent_ui

        self.setFixedSize(50, 50)
        self.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.setIcon(QtGui.QIcon(icon_path))
        self.setIconSize(QtCore.QSize(40, 40))

        # Transparency effect for inactive state
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)

        # Resize animation
        self.animation = QtCore.QPropertyAnimation(self, b"iconSize")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

        self.original_size = QtCore.QSize(40, 40)
        self.hover_size = QtCore.QSize(50, 50)
        self.disabled_size = QtCore.QSize(30, 30)
        self.is_hover_enabled = True

        # Connecting click handlers
        if direction == "left":
            self.clicked.connect(lambda: prev_page(self.parent_ui))
        elif direction == "right":
            self.clicked.connect(lambda: next_page(self.parent_ui))

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