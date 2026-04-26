import sys
import os
from PyQt6.QtWidgets import QMessageBox
from styles import MessageStyle


# чтобы при компиляции были видны иконки
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def show_message(parent, title, text, style_type="warning"):
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setText(text)

    if style_type == "warning":
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStyleSheet(MessageStyle.warning)
    elif style_type == "error":
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setStyleSheet(MessageStyle.error)
    elif style_type == "info":
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStyleSheet(MessageStyle.info)

    msg.exec()