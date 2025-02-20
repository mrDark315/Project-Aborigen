from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
from components.SearchBar import SearchBar
from components.CreatedByButton import CreatedByButton
from components.CloseButton import CloseButton
from components.NavArrows import AnimatedArrowButton
from components.SideFilter import SideFilter
from components.SortingButtons import SortingButtons
from func.search_func import handle_search, delay_search
from func.display_profile_games import display_profile_games

class ProfilePage(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Main Widget
        parent.setStyleSheet("background-color: #0E1621;")

        # Main Layout
        self.layout = QtWidgets.QVBoxLayout(self)

        # Top Layout
        self.search_filter_layout = QtWidgets.QHBoxLayout()
        self.search_filter_layout.setAlignment(QtCore.Qt.AlignCenter)

            # Margin from the left border of the window
        self.left_spacer = QtWidgets.QSpacerItem(40, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.search_filter_layout.addItem(self.left_spacer)

            # Created By Button
        self.created_by_btn = CreatedByButton(self)
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

            # Close Button
        self.close_btn = CloseButton(self.parent)
        self.search_filter_layout.addWidget(self.close_btn)

            # Margin from the right border of the window
        self.right_spacer = QtWidgets.QSpacerItem(60, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.search_filter_layout.addItem(self.right_spacer)



        # Bottom Layout
        self.bottom_container_layout = QtWidgets.QVBoxLayout()
        self.bottom_container_layout.setAlignment(Qt.AlignCenter)

            # Grid Navigation Layout
        self.grid_navigation_layout = QtWidgets.QHBoxLayout()
        self.grid_navigation_layout.setAlignment(Qt.AlignCenter)

            # Side Filter Layout
        self.side_filter = SideFilter(self)
        self.grid_navigation_layout.addWidget(self.side_filter)

            # Left arrow
        self.left_arrow = AnimatedArrowButton("img/Arrow_Left.png", self, "left")
        self.grid_navigation_layout.addWidget(self.left_arrow)

            # Grid Games
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setSpacing(20)
        self.grid_widget = QtWidgets.QWidget()
        self.grid_widget.setLayout(self.grid_layout)
        self.grid_widget.setVisible(True)

            # Container for sort and grid buttons
        self.grid_container_widget = QtWidgets.QWidget()
        self.grid_container_layout = QtWidgets.QVBoxLayout(self.grid_container_widget)
        self.grid_container_layout.setAlignment(Qt.AlignCenter)
        self.grid_container_layout.addWidget(self.grid_widget)

            # Common container to the layout with arrows
        self.grid_navigation_layout.addWidget(self.grid_container_widget)

            # Right arrow
        self.right_arrow = AnimatedArrowButton("img/Arrow_Right.png", self, "right")
        self.grid_navigation_layout.addWidget(self.right_arrow)

            # Container for sorting buttons
        self.sorting_buttons_layout = QtWidgets.QHBoxLayout()
        self.sorting_buttons_layout.setAlignment(Qt.AlignCenter)

            # Add SortingButtons inside a separate container
        self.sorting_buttons = SortingButtons(self)
        self.sorting_buttons_layout.addWidget(self.sorting_buttons, alignment=Qt.AlignCenter)

        # Add to Main Layout
        self.layout.addLayout(self.search_filter_layout)
        self.layout.addLayout(self.sorting_buttons_layout)
        self.layout.addLayout(self.grid_navigation_layout)

        # Load Games
        # self.filtered_games = list(cached_games_dict.values())
        # self.current_page = 0
        # display_game_icons(self)
        self.layout.addLayout(self.grid_layout)
        display_profile_games(self)

        # Connect Search Bar and Timer
        self.search_timer = QtCore.QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(lambda: handle_search(self))
        self.search_bar.textChanged.connect(lambda: delay_search(self))