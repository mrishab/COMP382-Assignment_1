from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt
from comp382_assignment_1.gui.app_config import AppConfig

class LeftSidebar(QFrame):
    def __init__(self, app_config: AppConfig, parent=None):
        super().__init__(parent)
        self.app_config = app_config
        self.setup_ui()

    def setup_ui(self):
        from comp382_assignment_1.gui.utils import load_stylesheet
        self.setStyleSheet(load_stylesheet('left_sidebar.css'))
        
        # Determine fixed width if needed, or let layout handle it. 
        # Typically sidebars have a fixed or max width.
        self.setFixedWidth(250)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 30, 20, 20)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

        # Title
        title_label = QLabel(self.app_config.left_sidebar_title)
        title_label.setObjectName("Title")
        layout.addWidget(title_label)
        
        # Separator or spacing
        layout.addSpacing(10)

        # Reference Points
        for text in self.app_config.left_sidebar_info_points:
            label = QLabel(text)
            label.setWordWrap(True)
            layout.addWidget(label)
        
        # Add stretch at the bottom to push content up
        layout.addStretch()
