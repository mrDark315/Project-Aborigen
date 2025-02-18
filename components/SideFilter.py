from PyQt5 import QtWidgets
import json
from func.search_func import handle_search
from func.sorting_side_filter import sort_games


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
        file_path = "store/SideFilterData.json"
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        developers = self.extract_developers(data)
        dropdown_titles = ["Sorting", "Developer", "Rating", "Price", "Release Date", "Platform", "Controller"]
        predefined_options = {
            "Sorting": ["Name (A-Z)", "Name (Z-A)", "Rating (High)", "Rating (Low)", "Release Date (New)", "Release Date (Old)"],
            "Rating": ["From 60 to 69", "From 70 to 79", "From 80 to 89", "From 90 to 94", "From 95 to 100"],
            "Price": ["Free", "Under $10", "$10-$30", "$30-$60", "Above $60"],
            "Platform": ["Windows", "Mac", "Linux"],
            "Release Date": ["2024", "2023", "2022", "2010-2021", "Before 2010"],
            "Controller": ["Full Support", "No Support"]
        }

        def truncate_text(text, max_length=16):
            return text if len(text) <= max_length else text[:max_length] + "..."

        for title in dropdown_titles:
            dropdown = QtWidgets.QComboBox()
            dropdown.addItem(f"All {title}")

            if title == "Developer":
                truncated_developers = [truncate_text(dev) for dev in developers]
                dropdown.addItems(truncated_developers)
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
            dev_list = game.get("developers", [])

            if isinstance(dev_list, str):
                dev_list = eval(dev_list) if dev_list.startswith("[") else [dev_list]

            developers.update(dev_list)

        return sorted(dev.strip() for dev in developers if dev.strip())