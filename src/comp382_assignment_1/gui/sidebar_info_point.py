from PySide6.QtWidgets import QLabel

class SidebarInfoPoint(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setWordWrap(True)
