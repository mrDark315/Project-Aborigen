from PyQt5 import QtWidgets
import json
from func.search_func import handle_search

class SideFilter(QtWidgets.QWidget):
    def __init__(self, parent_ui):
        super().__init__(parent_ui.main)
        self.parent_ui = parent_ui

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setMaximumSize(320, 820)
        self.setMinimumSize(320, 700)
        self.setStyleSheet("background-color: transparent; margin-left: 25;")

        self.load_filter_options()

    def load_filter_options(self):
        file_path = "store/data.json"
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        developers = self.extract_developers(data)
        dropdown_titles = ["Sorting", "Developer", "Rating", "Price", "Release Date", "Platform", "Controller"]
        predefined_options = {
            "Rating": ["From 60 to 69", "From 70 to 79", "From 80 to 89", "From 90 to 94", "From 95 to 100"],
            "Price": ["Free", "Under $10", "$10-$30", "$30-$60", "Above $60"],
            "Platform": ["Windows", "Mac", "Linux"],
            "Release Date": ["2024", "2023", "2022", "2010-2021", "Before 2010"],
            "Controller": ["Full Support", "No Support"]
        }

        for title in dropdown_titles:
            dropdown = QtWidgets.QComboBox()
            dropdown.addItem(f"All {title}")

            if title == "Developer":
                dropdown.addItems(developers)
            else:
                dropdown.addItems(predefined_options.get(title, []))

            dropdown.setStyleSheet("""
                QComboBox {background-color: #454C55; border: none; height: 50px; border-radius: 25px; padding-left: 30px; font-size: 28px; color: #000;}
                QComboBox::drop-down {background-color: transparent;}
                QComboBox QAbstractItemView {font-size: 20px; background-color: #454C55; color: #000; selection-background-color: #454C55; selection-color: #898989; border-radius: 10px; outline: none;}
            """)

            dropdown.currentIndexChanged.connect(lambda: handle_search(self.parent_ui))
            self.layout.addWidget(dropdown)

    def extract_developers(self, data):
        developers = set()
        for game in data:
            dev_list = game.get("developer", [])

            if isinstance(dev_list, str):
                dev_list = eval(dev_list) if dev_list.startswith("[") else [dev_list]

            developers.update(dev_list)

        return sorted(developers)
