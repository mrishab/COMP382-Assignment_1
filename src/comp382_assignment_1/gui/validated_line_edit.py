from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from comp382_assignment_1.gui.constants import CONTROL_KEY_MIN, CONTROL_KEY_MAX, CONTROL_MODIFIER, META_MODIFIER

class ValidatedLineEdit(QLineEdit):
    def __init__(self, allowed_chars=None, parent=None):
        super().__init__(parent)
        self.allowed_chars = allowed_chars if allowed_chars is not None else set()
        
    def keyPressEvent(self, event: QKeyEvent):
        text = event.text()
        key = event.key()
        
        # Always allow control keys (Backspace, Delete, Left, Right, etc.)
        is_control = (key < CONTROL_KEY_MIN) or (key > CONTROL_KEY_MAX) or \
                     (event.modifiers() & CONTROL_MODIFIER) or \
                     (event.modifiers() & META_MODIFIER)
        
        if is_control or not text:
             super().keyPressEvent(event)
             return

        if text in self.allowed_chars:
            super().keyPressEvent(event)
        else:
            ## Ignoring invalid characters
            pass
