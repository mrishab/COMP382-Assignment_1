from PySide6.QtWidgets import QPushButton, QLineEdit
from PySide6.QtCore import Qt

class KeyboardButton(QPushButton):
    def __init__(self, text, target_input: QLineEdit, parent=None):
        super().__init__(text, parent)
        self.target_input = target_input
        self.setFixedSize(40, 40)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        # Default behavior: insert text
        self.target_input.insert(self.text())
        self.target_input.setFocus()

class BackspaceButton(KeyboardButton):
    def __init__(self, target_input: QLineEdit, parent=None):
        super().__init__("⌫", target_input, parent) # Using backspace symbol

    def on_clicked(self):
        self.target_input.backspace()
        self.target_input.setFocus()
