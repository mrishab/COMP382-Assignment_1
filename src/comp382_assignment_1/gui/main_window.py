from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QFrame
from PySide6.QtCore import Qt
from comp382_assignment_1.gui.app_config import AppConfig
from comp382_assignment_1.gui.left_sidebar import LeftSidebar
from comp382_assignment_1.gui.section_step_1 import SectionStep1
from comp382_assignment_1.gui.section_step_2 import SectionStep2

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
        self.right_panel = QWidget()
        self.right_panel.setObjectName("RightPanel")
        
        from comp382_assignment_1.gui.utils import load_stylesheet
        self.setStyleSheet(load_stylesheet('main_window.css'))
        
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(40, 40, 40, 40)
        right_layout.setSpacing(20)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.right_panel.setLayout(right_layout)
        
        main_layout.addWidget(self.right_panel, stretch=1)

        # --- Right Panel Content ---

        # Header Title
        # Icon could be added here if available, using text with emoji for now
        self.header_title = QLabel(f"⚡ {self.app_config.main_header_title}")
        self.header_title.setObjectName("HeaderTitle")
        right_layout.addWidget(self.header_title)

        # Dictionary / Alphabet info
        self.alphabet_label = QLabel(self.app_config.alphabet_text)
        self.alphabet_label.setObjectName("AlphabetLabel")
        right_layout.addWidget(self.alphabet_label)

        # Step 1 Section
        self.step1 = SectionStep1(app_config)
        right_layout.addWidget(self.step1)

        # Horizontal Line Separator
        line = QFrame()
        line.setObjectName("Separator")
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        right_layout.addWidget(line)

        # Step 2 Section
        self.step2 = SectionStep2(app_config)
        right_layout.addWidget(self.step2)

        # Spacer (push footer down if window is large, or just spacing)
        right_layout.addStretch()

        # Footer "How to use this tool"
        footer_container = QWidget()
        footer_layout = QVBoxLayout()
        footer_layout.setContentsMargins(0, 20, 0, 0)
        footer_container.setLayout(footer_layout)

        footer_title = QLabel(self.app_config.footer_title)
        footer_title.setObjectName("FooterTitle")
        footer_layout.addWidget(footer_title)

        for point in self.app_config.footer_points:
            p_label = QLabel(f"• {point}")
            p_label.setObjectName("FooterPoint")
            footer_layout.addWidget(p_label)
        
        right_layout.addWidget(footer_container)

