from PyQt5 import QtWidgets

class ProfilePage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Создаём основной макет
        layout = QtWidgets.QVBoxLayout(self)

        # Заголовок
        title = QtWidgets.QLabel("Страница профиля")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        # Заглушка информации о профиле
        profile_info = QtWidgets.QLabel("Здесь будет информация о профиле")
        layout.addWidget(profile_info)

        # Кнопка назад
        self.back_button = QtWidgets.QPushButton("Назад")
        self.back_button.setStyleSheet("padding: 10px; font-size: 18px;")
        layout.addWidget(self.back_button)

        self.setLayout(layout)
