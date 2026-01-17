from PySide6.QtWidgets import QLabel

class FooterPoint(QLabel):
    def __init__(self, text, parent=None):
        # Add bullet point prefix here for consistency
        super().__init__(f"• {text}", parent)
        self.setObjectName("FooterPoint")
