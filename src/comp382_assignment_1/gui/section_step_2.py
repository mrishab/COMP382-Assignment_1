from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from comp382_assignment_1.gui.app_config import AppConfig
from comp382_assignment_1.gui.validated_line_edit import ValidatedLineEdit
from comp382_assignment_1.gui.virtual_keyboard import VirtualKeyboard
from comp382_assignment_1.gui.status_indicator import StatusIndicator
from comp382_assignment_1.gui.utils import load_stylesheet
from comp382_assignment_1.logic.matcher import match

class SectionStep2(QWidget):
    def __init__(self, app_config: AppConfig, parent=None):
        super().__init__(parent)
        self.app_config = app_config
        self.current_regex = ""
        self.setup_ui()
        
    def setup_ui(self):
        self.setStyleSheet(load_stylesheet('section_step_2.css'))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 20)
        self.setLayout(layout)

        # Heading
        self.heading = QLabel(self.app_config.section_2_title)
        self.heading.setObjectName("Heading")
        layout.addWidget(self.heading)

        # Subtext
        self.sub_label = QLabel(self.app_config.section_2_subtext)
        self.sub_label.setObjectName("SubLabel")
        layout.addWidget(self.sub_label)

        # Input Row (Input + Result Label)
        input_row = QHBoxLayout()
        input_row.setSpacing(10)
        
        # Input
        self.input_field = ValidatedLineEdit(allowed_chars=self.app_config.valid_test_string_chars)
        self.input_field.setPlaceholderText(self.app_config.section_2_placeholder)
        input_row.addWidget(self.input_field, stretch=1)

        # Result Status Indicator
        self.result_status = StatusIndicator()
        input_row.addWidget(self.result_status)
        
        layout.addLayout(input_row)

        # Virtual Keyboard
        self.keyboard = VirtualKeyboard(self.app_config.test_string_keyboard_keys, self.input_field)
        layout.addWidget(self.keyboard)
        
        # Connect signals
        self.input_field.textChanged.connect(lambda: self.update_match(self.current_regex))
        
        # Initialize state from logic
        self.update_match("")

    def update_match(self, regex):
        self.current_regex = regex
        test_string = self.input_field.text()
            
        result = match(self.current_regex, test_string)
        self.result_status.set_status(result, "Accepted", "Rejected")
