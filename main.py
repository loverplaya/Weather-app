import sys
import requests
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QListWidget, QVBoxLayout,
                             QHBoxLayout, QMessageBox, QFrame, QStyle)
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QLinearGradient, QColor, QBrush
from background import background
from styles import ButtonStyle, LineEdit_Style
from screens import main_screen


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle("Прогноз погоды")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # Фон
        self.bg = background(self)
        self.bg.apply_gradient()

        # Главный экран
        self.main_screen = main_screen(self)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.main_screen)
        self.setLayout(main_layout)

    # Обновление позиции поля при изменении размера окна
    def resizeEvent(self, event):
        if hasattr(self, 'main_screen'):
            self.main_screen.update_position(self.width())
        super().resizeEvent(event)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())