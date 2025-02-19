from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
from components.SearchBar import SearchBar
from components.ProfileButton import ProfileButton
from components.CreatedByButton import CreatedByButton
from components.NavArrows import AnimatedArrowButton
from components.SideFilter import SideFilter
from func.search_func import handle_search, delay_search, cached_games_dict
from func.display_game import display_game_icons

class HomePage(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Main Widget
        # self.parent = QtWidgets.QWidget(parent)
        parent.setStyleSheet("background-color: #0E1621;")

        # Main Layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Top Layout
        self.search_filter_layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.search_filter_layout.setAlignment(QtCore.Qt.AlignCenter)
            # Margin from the left border of the window
        self.left_spacer = QtWidgets.QSpacerItem(40, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.search_filter_layout.addItem(self.left_spacer)
            # Created By Button
        self.created_by_btn = CreatedByButton(parent)
        self.search_filter_layout.addWidget(self.created_by_btn)
            # Adaptive distance between Created By Button and Search Bar
        self.expand_spacer1 = QtWidgets.QSpacerItem(1, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.search_filter_layout.addItem(self.expand_spacer1)
            # Search bar
        self.search_bar = SearchBar(self)
        self.search_filter_layout.addWidget(self.search_bar)
            # Adaptive distance between Search Bar and Profile Button
        self.expand_spacer2 = QtWidgets.QSpacerItem(1, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.search_filter_layout.addItem(self.expand_spacer2)
            # Profile Button
        self.profile_btn = ProfileButton(parent)
        self.search_filter_layout.addWidget(self.profile_btn)
            # Margin from the right border of the window
        self.right_spacer = QtWidgets.QSpacerItem(60, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.search_filter_layout.addItem(self.right_spacer)

        # Bottom Layout
        self.grid_navigation_layout = QtWidgets.QHBoxLayout()
        self.grid_navigation_layout.setAlignment(Qt.AlignCenter)
            # Side Filter Layout
        self.side_filter = SideFilter(self)
        self.grid_navigation_layout.addWidget(self.side_filter)
            # Left arrow
        self.left_arrow = AnimatedArrowButton("img/Arrow_Left.png", self, "left")
        self.grid_navigation_layout.addWidget(self.left_arrow)
            # Grid Layout
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setSpacing(20)
        self.grid_widget = QtWidgets.QWidget()
        self.grid_widget.setLayout(self.grid_layout)
        self.grid_widget.setVisible(True)
        self.grid_navigation_layout.addWidget(self.grid_widget)
            # Right arrow
        self.right_arrow = AnimatedArrowButton("img/Arrow_Right.png", self, "right")
        self.grid_navigation_layout.addWidget(self.right_arrow)

        # Add to Main Layout
        self.layout.addLayout(self.search_filter_layout)
        self.layout.addLayout(self.grid_navigation_layout)

        # Load Games
        self.filtered_games = list(cached_games_dict.values())
        self.current_page = 0
        display_game_icons(self)

        # Connect Search Bar and Timer
        self.search_timer = QtCore.QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(lambda: handle_search(self))
        self.search_bar.textChanged.connect(lambda: delay_search(self))