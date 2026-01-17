from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt
from comp382_assignment_1.gui.app_config import AppConfig
from comp382_assignment_1.gui.components import ValidatedLineEdit, VirtualKeyboard

class SectionStep2(QWidget):
    def __init__(self, app_config: AppConfig, parent=None):
        super().__init__(parent)
        self.app_config = app_config
        self.setup_ui()
    def setup_ui(self):
        from comp382_assignment_1.gui.utils import load_stylesheet
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

        # Input
        self.input_field = ValidatedLineEdit(allowed_chars=self.app_config.valid_test_string_chars)
        self.input_field.setPlaceholderText(self.app_config.section_2_placeholder)
        layout.addWidget(self.input_field)

        # Virtual Keyboard
        self.keyboard = VirtualKeyboard(self.app_config.test_string_keyboard_keys, self.input_field)
        layout.addWidget(self.keyboard)

        # Result Label (Static visualization for now as per image)
        # Using the success template with 'aba' to match the screenshot
        sample_result = self.app_config.section_2_status_success_template.format("aba")
        self.result_label = QLabel(f"🎉 {sample_result}") 
        self.result_label.setObjectName("ResultLabel")
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)
