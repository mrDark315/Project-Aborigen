from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(2560, 1440))
        self.main = QtWidgets.QWidget(MainWindow)
        self.main.setStyleSheet("background-color: rgb(14, 22, 33);")
        self.main.setObjectName("main")
        self.btn_search = QtWidgets.QLabel(self.main)
        self.btn_search.setGeometry(QtCore.QRect(660, 36, 960, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.btn_search.setStyleSheet("background-color: #454C55;\n"
"color: #898989;\n"
"border-radius: 35px;\n"
"padding-left: 100px;")
        self.btn_search.setObjectName("btn_search")
        self.btn_profile = QtWidgets.QLabel(self.main)
        self.btn_profile.setGeometry(QtCore.QRect(1750, 36, 100, 100))
        self.btn_profile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_profile.setStyleSheet("")
        self.btn_profile.setText("")
        self.btn_profile.setPixmap(QtGui.QPixmap("img/Profile.png"))
        self.btn_profile.setObjectName("btn_profile")
        self.btn_sort = QtWidgets.QLabel(self.main)
        self.btn_sort.setGeometry(QtCore.QRect(25, 174, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_sort.setFont(font)
        self.btn_sort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sort.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;")
        self.btn_sort.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_sort.setObjectName("btn_sort")
        self.label_2 = QtWidgets.QLabel(self.main)
        self.label_2.setGeometry(QtCore.QRect(35, 49, 300, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("color: #454C55; \n"
"background-color: #898989;\n"
"border-radius: 35px;\n"
"border: 2px solid #454C55;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_filter_pub = QtWidgets.QLabel(self.main)
        self.btn_filter_pub.setGeometry(QtCore.QRect(25, 284, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_filter_pub.setFont(font)
        self.btn_filter_pub.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_filter_pub.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;")
        self.btn_filter_pub.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_filter_pub.setObjectName("btn_filter_pub")
        self.btn_frlter_developer = QtWidgets.QLabel(self.main)
        self.btn_frlter_developer.setGeometry(QtCore.QRect(25, 394, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_frlter_developer.setFont(font)
        self.btn_frlter_developer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_frlter_developer.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;")
        self.btn_frlter_developer.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_frlter_developer.setObjectName("btn_frlter_developer")
        self.btn_filter_rating = QtWidgets.QLabel(self.main)
        self.btn_filter_rating.setGeometry(QtCore.QRect(25, 504, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_filter_rating.setFont(font)
        self.btn_filter_rating.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_filter_rating.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;")
        self.btn_filter_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_filter_rating.setObjectName("btn_filter_rating")
        self.btn_filter_controller = QtWidgets.QLabel(self.main)
        self.btn_filter_controller.setGeometry(QtCore.QRect(25, 614, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_filter_controller.setFont(font)
        self.btn_filter_controller.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_filter_controller.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;")
        self.btn_filter_controller.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_filter_controller.setObjectName("btn_filter_controller")
        self.label_7 = QtWidgets.QLabel(self.main)
        self.label_7.setGeometry(QtCore.QRect(25, 724, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.main)
        self.label_8.setGeometry(QtCore.QRect(25, 834, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.main)
        self.label_9.setGeometry(QtCore.QRect(25, 944, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.main)
        self.label_10.setGeometry(QtCore.QRect(370, 554, 40, 80))
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("img/Arrow Left.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.main)
        self.label_11.setGeometry(QtCore.QRect(1860, 554, 40, 80))
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("img/Arrow Right.png"))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_search.setText(_translate("MainWindow", "Введіть незву гри..."))
        self.btn_sort.setText(_translate("MainWindow", "Сортування ▼"))
        self.label_2.setText(_translate("MainWindow", "Created by:"))
        self.btn_filter_pub.setText(_translate("MainWindow", "Видавець ▼"))
        self.btn_frlter_developer.setText(_translate("MainWindow", "Розробник ▼"))
        self.btn_filter_rating.setText(_translate("MainWindow", "Рейтинг ▼"))
        self.btn_filter_controller.setText(_translate("MainWindow", "Контроллер ▼"))
        self.label_7.setText(_translate("MainWindow", "Платформа ▼"))
        self.label_8.setText(_translate("MainWindow", "Дата релізу ▼"))
        self.label_9.setText(_translate("MainWindow", "Вікове обм. ▼"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())