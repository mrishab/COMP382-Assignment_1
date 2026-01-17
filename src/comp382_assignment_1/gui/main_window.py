from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from comp382_assignment_1.gui.app_config import AppConfig
from comp382_assignment_1.gui.left_sidebar import LeftSidebar
from comp382_assignment_1.gui.right_panel import RightPanel

class MainWindow(QMainWindow):
    def __init__(self, app_config: AppConfig):
        super().__init__()
        self.app_config = app_config
        self.resize(app_config.window_width, app_config.window_height)
        self.setWindowTitle(app_config.window_title)

        # Main Layout (Horizontal split)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)

        # 1. Left Sidebar
        self.sidebar = LeftSidebar(app_config)
        main_layout.addWidget(self.sidebar)

        # 2. Right Panel (Main Content)
        self.right_panel = RightPanel(app_config)
        main_layout.addWidget(self.right_panel, stretch=1)
