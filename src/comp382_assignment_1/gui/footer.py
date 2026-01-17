from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from comp382_assignment_1.gui.app_config import AppConfig
from comp382_assignment_1.gui.footer_point import FooterPoint

class Footer(QWidget):
    def __init__(self, app_config: AppConfig, parent=None):
        super().__init__(parent)
        self.app_config = app_config
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 20, 0, 0)
        layout.setSpacing(5)

        footer_title = QLabel(self.app_config.footer_title)
        footer_title.setObjectName("FooterTitle")
        layout.addWidget(footer_title)

        for point in self.app_config.footer_points:
            p_label = FooterPoint(point)
            layout.addWidget(p_label)
