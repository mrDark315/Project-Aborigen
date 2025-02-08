from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1077)
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
"padding-left: 85px;")
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
"border-radius: 35px;\n"
"padding-left: 20px;")
        self.btn_sort.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.btn_sort.setObjectName("btn_sort")
        self.btn_created_by = QtWidgets.QLabel(self.main)
        self.btn_created_by.setGeometry(QtCore.QRect(35, 49, 300, 75))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_created_by.setFont(font)
        self.btn_created_by.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_created_by.setStyleSheet("color: #454C55; \n"
"background-color: #898989;\n"
"border-radius: 35px;\n"
"border: 2px solid #454C55;")
        self.btn_created_by.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_created_by.setObjectName("btn_created_by")
        self.btn_filter_pub = QtWidgets.QLabel(self.main)
        self.btn_filter_pub.setGeometry(QtCore.QRect(25, 284, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_filter_pub.setFont(font)
        self.btn_filter_pub.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_filter_pub.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;\n"
"padding-left: 20px;")
        self.btn_filter_pub.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.btn_filter_pub.setObjectName("btn_filter_pub")
        self.btn_frlter_developer = QtWidgets.QLabel(self.main)
        self.btn_frlter_developer.setGeometry(QtCore.QRect(25, 394, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_frlter_developer.setFont(font)
        self.btn_frlter_developer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_frlter_developer.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;\n"
"padding-left: 20px;")
        self.btn_frlter_developer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.btn_frlter_developer.setObjectName("btn_frlter_developer")
        self.btn_filter_rating = QtWidgets.QLabel(self.main)
        self.btn_filter_rating.setGeometry(QtCore.QRect(25, 504, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_filter_rating.setFont(font)
        self.btn_filter_rating.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_filter_rating.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;\n"
"padding-left: 20px;")
        self.btn_filter_rating.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.btn_filter_rating.setObjectName("btn_filter_rating")
        self.btn_filter_controller = QtWidgets.QLabel(self.main)
        self.btn_filter_controller.setGeometry(QtCore.QRect(25, 614, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_filter_controller.setFont(font)
        self.btn_filter_controller.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_filter_controller.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;\n"
"padding-left: 20px;")
        self.btn_filter_controller.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.btn_filter_controller.setObjectName("btn_filter_controller")
        self.btn_filter_platform = QtWidgets.QLabel(self.main)
        self.btn_filter_platform.setGeometry(QtCore.QRect(25, 724, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_filter_platform.setFont(font)
        self.btn_filter_platform.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_filter_platform.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;\n"
"padding-left: 20px;")
        self.btn_filter_platform.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.btn_filter_platform.setObjectName("btn_filter_platform")
        self.btn_filter_release = QtWidgets.QLabel(self.main)
        self.btn_filter_release.setGeometry(QtCore.QRect(25, 834, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_filter_release.setFont(font)
        self.btn_filter_release.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_filter_release.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;\n"
"padding-left: 20px;")
        self.btn_filter_release.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.btn_filter_release.setObjectName("btn_filter_release")
        self.btn_filter_age_rating = QtWidgets.QLabel(self.main)
        self.btn_filter_age_rating.setGeometry(QtCore.QRect(25, 944, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.btn_filter_age_rating.setFont(font)
        self.btn_filter_age_rating.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_filter_age_rating.setStyleSheet("color: #000;\n"
"background-color: #454C55;\n"
"border-radius: 35px;\n"
"padding-left: 20px;")
        self.btn_filter_age_rating.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.btn_filter_age_rating.setObjectName("btn_filter_age_rating")
        self.nav_arrow_left = QtWidgets.QLabel(self.main)
        self.nav_arrow_left.setGeometry(QtCore.QRect(370, 554, 40, 80))
        self.nav_arrow_left.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nav_arrow_left.setText("")
        self.nav_arrow_left.setPixmap(QtGui.QPixmap("img/Arrow Left.png"))
        self.nav_arrow_left.setObjectName("nav_arrow_left")
        self.nav_arrow_right = QtWidgets.QLabel(self.main)
        self.nav_arrow_right.setGeometry(QtCore.QRect(1860, 554, 40, 80))
        self.nav_arrow_right.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nav_arrow_right.setText("")
        self.nav_arrow_right.setPixmap(QtGui.QPixmap("img/Arrow Right.png"))
        self.nav_arrow_right.setObjectName("nav_arrow_right")
        self.icon_search = QtWidgets.QLabel(self.main)
        self.icon_search.setGeometry(QtCore.QRect(685, 61, 50, 50))
        self.icon_search.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.icon_search.setStyleSheet("background-color: #454C55;")
        self.icon_search.setText("")
        self.icon_search.setPixmap(QtGui.QPixmap("img/Search.png"))
        self.icon_search.setObjectName("icon_search")
        self.icon_arrow_down_sorting = QtWidgets.QLabel(self.main)
        self.icon_arrow_down_sorting.setGeometry(QtCore.QRect(280, 204, 40, 20))
        self.icon_arrow_down_sorting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_arrow_down_sorting.setStyleSheet("background-color: #454C55;")
        self.icon_arrow_down_sorting.setText("")
        self.icon_arrow_down_sorting.setPixmap(QtGui.QPixmap("img/Arrow Down Black.png"))
        self.icon_arrow_down_sorting.setObjectName("icon_arrow_down_sorting")
        self.icon_arrow_down_publisher = QtWidgets.QLabel(self.main)
        self.icon_arrow_down_publisher.setGeometry(QtCore.QRect(280, 314, 40, 20))
        self.icon_arrow_down_publisher.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_arrow_down_publisher.setStyleSheet("background-color: #454C55;")
        self.icon_arrow_down_publisher.setText("")
        self.icon_arrow_down_publisher.setPixmap(QtGui.QPixmap("img/Arrow Down Black.png"))
        self.icon_arrow_down_publisher.setObjectName("icon_arrow_down_publisher")
        self.icon_arrow_down_developer = QtWidgets.QLabel(self.main)
        self.icon_arrow_down_developer.setGeometry(QtCore.QRect(280, 424, 40, 20))
        self.icon_arrow_down_developer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_arrow_down_developer.setStyleSheet("background-color: #454C55;")
        self.icon_arrow_down_developer.setText("")
        self.icon_arrow_down_developer.setPixmap(QtGui.QPixmap("img/Arrow Down Black.png"))
        self.icon_arrow_down_developer.setObjectName("icon_arrow_down_developer")
        self.icon_arrow_down_controller = QtWidgets.QLabel(self.main)
        self.icon_arrow_down_controller.setGeometry(QtCore.QRect(280, 644, 40, 20))
        self.icon_arrow_down_controller.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_arrow_down_controller.setStyleSheet("background-color: #454C55;")
        self.icon_arrow_down_controller.setText("")
        self.icon_arrow_down_controller.setPixmap(QtGui.QPixmap("img/Arrow Down Black.png"))
        self.icon_arrow_down_controller.setObjectName("icon_arrow_down_controller")
        self.icon_arrow_down_rating = QtWidgets.QLabel(self.main)
        self.icon_arrow_down_rating.setGeometry(QtCore.QRect(280, 534, 40, 20))
        self.icon_arrow_down_rating.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_arrow_down_rating.setStyleSheet("background-color: #454C55;")
        self.icon_arrow_down_rating.setText("")
        self.icon_arrow_down_rating.setPixmap(QtGui.QPixmap("img/Arrow Down Black.png"))
        self.icon_arrow_down_rating.setObjectName("icon_arrow_down_rating")
        self.icon_arrow_down_platform = QtWidgets.QLabel(self.main)
        self.icon_arrow_down_platform.setGeometry(QtCore.QRect(280, 754, 40, 20))
        self.icon_arrow_down_platform.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_arrow_down_platform.setStyleSheet("background-color: #454C55;")
        self.icon_arrow_down_platform.setText("")
        self.icon_arrow_down_platform.setPixmap(QtGui.QPixmap("img/Arrow Down Black.png"))
        self.icon_arrow_down_platform.setObjectName("icon_arrow_down_platform")
        self.icon_arrow_down_release = QtWidgets.QLabel(self.main)
        self.icon_arrow_down_release.setGeometry(QtCore.QRect(280, 864, 40, 20))
        self.icon_arrow_down_release.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_arrow_down_release.setStyleSheet("background-color: #454C55;")
        self.icon_arrow_down_release.setText("")
        self.icon_arrow_down_release.setPixmap(QtGui.QPixmap("img/Arrow Down Black.png"))
        self.icon_arrow_down_release.setObjectName("icon_arrow_down_release")
        self.icon_arrow_down_age_rating = QtWidgets.QLabel(self.main)
        self.icon_arrow_down_age_rating.setGeometry(QtCore.QRect(280, 974, 40, 20))
        self.icon_arrow_down_age_rating.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_arrow_down_age_rating.setStyleSheet("background-color: #454C55;")
        self.icon_arrow_down_age_rating.setText("")
        self.icon_arrow_down_age_rating.setPixmap(QtGui.QPixmap("img/Arrow Down Black.png"))
        self.icon_arrow_down_age_rating.setObjectName("icon_arrow_down_age_rating")
        self.item_game = QtWidgets.QFrame(self.main)
        self.item_game.setGeometry(QtCore.QRect(430, 174, 460, 400))
        self.item_game.setStyleSheet("background-color: rgb(69, 76, 85);\n"
"border-radius: 50px;")
        self.item_game.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.item_game.setFrameShadow(QtWidgets.QFrame.Raised)
        self.item_game.setObjectName("item_game")
        self.image_game = QtWidgets.QLabel(self.item_game)
        self.image_game.setGeometry(QtCore.QRect(0, 0, 460, 215))
        self.image_game.setStyleSheet("border-top-left-radius: 50px;\n"
"background-color: rgb(204, 1, 4);\n"
"border-top-right-radius: 50px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"")
        self.image_game.setText("")
        self.image_game.setScaledContents(True)
        self.image_game.setObjectName("image_game")
        self.name_game = QtWidgets.QLabel(self.item_game)
        self.name_game.setGeometry(QtCore.QRect(0, 220, 369, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(32)
        self.name_game.setFont(font)
        self.name_game.setStyleSheet("color: #fff;\n"
"padding-left: 15px;\n"
"padding-top: 5px;\n"
"")
        self.name_game.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.name_game.setObjectName("name_game")
        self.rating_game = QtWidgets.QLabel(self.item_game)
        self.rating_game.setGeometry(QtCore.QRect(0, 340, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.rating_game.setFont(font)
        self.rating_game.setStyleSheet("color: #fff;\n"
"padding-left: 15px;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 0px;")
        self.rating_game.setObjectName("rating_game")
        self.controller_game = QtWidgets.QLabel(self.item_game)
        self.controller_game.setGeometry(QtCore.QRect(392, 240, 42, 27))
        self.controller_game.setText("")
        self.controller_game.setPixmap(QtGui.QPixmap("img/Controller_On.png"))
        self.controller_game.setObjectName("controller_game")
        self.favorites_game = QtWidgets.QLabel(self.item_game)
        self.favorites_game.setGeometry(QtCore.QRect(395, 340, 40, 38))
        self.favorites_game.setText("")
        self.favorites_game.setPixmap(QtGui.QPixmap("img/Star_Fill.png"))
        self.favorites_game.setObjectName("favorites_game")
        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_search.setText(_translate("MainWindow", "Enter the name of the game..."))
        self.btn_sort.setText(_translate("MainWindow", "Sorting"))
        self.btn_created_by.setText(_translate("MainWindow", "Created by:"))
        self.btn_filter_pub.setText(_translate("MainWindow", "Publisher"))
        self.btn_frlter_developer.setText(_translate("MainWindow", "Developer"))
        self.btn_filter_rating.setText(_translate("MainWindow", "Rating"))
        self.btn_filter_controller.setText(_translate("MainWindow", "Controller"))
        self.btn_filter_platform.setText(_translate("MainWindow", "Platform"))
        self.btn_filter_release.setText(_translate("MainWindow", "Release"))
        self.btn_filter_age_rating.setText(_translate("MainWindow", "Age Rating"))
        self.name_game.setText(_translate("MainWindow", "{name}"))
        self.rating_game.setText(_translate("MainWindow", "Metecritic: {rating}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
