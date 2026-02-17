import sys
import requests
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QListWidget, QVBoxLayout,
                             QHBoxLayout, QMessageBox, QFrame)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QLinearGradient, QColor, QBrush
from background import background




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
        #
        self.bg = background(self)
        self.bg.apply_gradient()
        #
        # Поле ввода города
        lineEdit_WriteCity = QLineEdit(self)
        lineEdit_WriteCity.setPlaceholderText("Введите город")
        lineEdit_WriteCity.setMinimumWidth(300)
        #

        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(lineEdit_WriteCity)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
