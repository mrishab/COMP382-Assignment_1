from PySide6.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from comp382_assignment_1.gui.utils import load_stylesheet

class ValidatedLineEdit(QLineEdit):
    def __init__(self, allowed_chars=None, parent=None):
        super().__init__(parent)
        self.allowed_chars = allowed_chars if allowed_chars is not None else set()
        
    def keyPressEvent(self, event: QKeyEvent):
        text = event.text()
        key = event.key()
        
        # Always allow control keys (Backspace, Delete, Left, Right, etc.)
        # Qt keys are integers. 
        # Backspace: 16777219, Delete: 16777223, Left: 16777234, Right: 16777236
        # Copy/Paste using modifiers should also be considered if we want to be strict,
        # but for now we focus on typing characters.
        
        is_control = (event.key() < 0) or (event.key() > 0x01000000) or (event.modifiers() & Qt.KeyboardModifier.ControlModifier) or (event.modifiers() & Qt.KeyboardModifier.MetaModifier)
        
        if is_control or not text:
             super().keyPressEvent(event)
             return

        if text in self.allowed_chars:
            super().keyPressEvent(event)
        else:
            ## Ignoring invalid characters
            pass

class VirtualKeyboard(QWidget):
    def __init__(self, keys, target_input: QLineEdit, parent=None):
        super().__init__(parent)
        self.keys = keys
        self.target_input = target_input
        self.setup_ui()
        
    def setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 10, 0, 0)
        layout.setSpacing(5)
        self.setLayout(layout)
        
        self.setStyleSheet(load_stylesheet('components.css'))
        
        for key in self.keys:
            btn = QPushButton(key)
            btn.setFixedSize(40, 40)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            # Style is now handled by class stylesheet
            btn.clicked.connect(lambda checked=False, k=key: self.on_key_clicked(k))
            layout.addWidget(btn)
            
        layout.addStretch() # Push left alignment
            
    def on_key_clicked(self, key):
        self.target_input.insert(key)
        self.target_input.setFocus()
