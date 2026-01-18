from comp382_assignment_1.common.symbols import STRING_SYMBOLS
from comp382_assignment_1.gui.heading_label import HeadingLabel
from comp382_assignment_1.gui.text import Text
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from comp382_assignment_1.gui.app_config import AppConfig
from comp382_assignment_1.gui.virtual_keyboard import VirtualKeyboard
from comp382_assignment_1.gui.input_bar import InputBar
from comp382_assignment_1.logic.matcher import match
from comp382_assignment_1.logic.regex_validator import validate_regex

class SectionStep2(QWidget):
    def __init__(self, app_config: AppConfig, parent=None):
        super().__init__(parent)
        self.app_config = app_config
        self.current_regex = ""
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 20)
        self.setLayout(layout)

        # Heading
        self.heading = HeadingLabel(self.app_config.section_2_heading)
        layout.addWidget(self.heading)

        # Subtext
        self.sub_label = Text(self.app_config.section_2_subheading)
        layout.addWidget(self.sub_label)

        self.string_input_bar = InputBar(
            placeholder_text=self.app_config.section_2_input_placeholder,
            allowed_chars=STRING_SYMBOLS,
            valid_text=self.app_config.section_2_status_text_valid,
            invalid_text=self.app_config.section_2_status_text_invalid,
            empty_text=self.app_config.section_2_status_text_empty,
            validator_func=lambda text: None if not validate_regex(self.current_regex) else match(self.current_regex, text)
        )
        layout.addWidget(self.string_input_bar)

        # Virtual Keyboard
        self.keyboard = VirtualKeyboard(STRING_SYMBOLS, self.string_input_bar.input_field)
        layout.addWidget(self.keyboard)

        # Connect signals
        self.string_input_bar.textChanged.connect(lambda: self.update_match(self.current_regex))

        # Initialize state
        self.update_match("")

    def update_match(self, regex):
        self.current_regex = regex
        self.string_input_bar.refresh_validation()
