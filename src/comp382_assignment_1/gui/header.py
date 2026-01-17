from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from comp382_assignment_1.gui.app_config import AppConfig

class Header(QWidget):
    def __init__(self, app_config: AppConfig, parent=None):
        super().__init__(parent)
        self.app_config = app_config
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        # Header Title
        self.header_title = QLabel(f"⚡ {self.app_config.main_header_title}")
        self.header_title.setObjectName("HeaderTitle")
        layout.addWidget(self.header_title)

        # Dictionary / Alphabet info
        self.alphabet_label = QLabel(self.app_config.alphabet_text)
        self.alphabet_label.setObjectName("AlphabetLabel")
        layout.addWidget(self.alphabet_label)
