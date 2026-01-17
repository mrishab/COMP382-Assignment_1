from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt
from comp382_assignment_1.gui.app_config import AppConfig
from comp382_assignment_1.gui.validated_line_edit import ValidatedLineEdit
from comp382_assignment_1.gui.virtual_keyboard import VirtualKeyboard
from comp382_assignment_1.gui.utils import load_stylesheet

class SectionStep1(QWidget):
    def __init__(self, app_config: AppConfig, parent=None):
        super().__init__(parent)
        self.app_config = app_config
        self.setup_ui()
    def setup_ui(self):
        self.setStyleSheet(load_stylesheet('section_step_1.css'))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 20, 0, 20)
        self.setLayout(layout)

        # 1. Heading
        self.heading = QLabel(self.app_config.section_1_title)
        self.heading.setObjectName("Heading")
        layout.addWidget(self.heading)

        # "Enter R:" Label
        self.sub_label = QLabel(self.app_config.section_1_subtext)
        self.sub_label.setObjectName("SubLabel")
        layout.addWidget(self.sub_label)

        # Input Row (Input + Button)
        input_row_layout = QHBoxLayout()
        input_row_layout.setSpacing(10)

        # Use ValidatedLineEdit
        self.input_field = ValidatedLineEdit(allowed_chars=self.app_config.valid_regex_chars)
        self.input_field.setPlaceholderText(self.app_config.section_1_placeholder)
        input_row_layout.addWidget(self.input_field)

        self.validate_btn = QPushButton(self.app_config.section_1_button_text)
        # Add checkmark icon conceptually (text for now or unicode) 
        # Unicode checkmark: ✓
        self.validate_btn.setText(f"✓ {self.app_config.section_1_button_text}")
        self.validate_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        # Fixed width for button maybe? Or let it expand slightly.
        self.validate_btn.setFixedWidth(140) 

        input_row_layout.addWidget(self.validate_btn)
        
        layout.addLayout(input_row_layout)

        # Virtual Keyboard
        self.keyboard = VirtualKeyboard(self.app_config.virtual_keyboard_keys, self.input_field)
        layout.addWidget(self.keyboard)

