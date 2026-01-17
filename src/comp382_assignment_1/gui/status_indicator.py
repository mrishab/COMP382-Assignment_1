from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

class StatusIndicator(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setFixedWidth(140)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setObjectName("StatusIndicator")

    def set_status(self, is_valid: bool, success_text: str, failure_text: str):
        if is_valid:
            self.setText(f"✓ {success_text}")
            self.setProperty("valid", True)
        else:
            self.setText(f"✗ {failure_text}")
            self.setProperty("valid", False)
        
        # Refresh style to apply variations if defined in CSS
        self.style().unpolish(self)
        self.style().polish(self)
