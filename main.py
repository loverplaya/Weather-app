import sys
import requests
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QListWidget, QVBoxLayout,
                             QHBoxLayout, QMessageBox, QFrame, QStyle)
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QLinearGradient, QColor, QBrush
from background import background
from styles import ButtonStyle, LineEdit_Style


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

        # Поле ввода города
        lineEdit_WriteCity = QLineEdit(self)
        lineEdit_WriteCity.setPlaceholderText("Введите город")
        lineEdit_WriteCity.setMinimumWidth(300)
        lineEdit_WriteCity.setMinimumHeight(35)
        lineEdit_WriteCity.setStyleSheet(LineEdit_Style.writeCity_LineEdit)


        # кнопка
        self.result_btn = QPushButton(" Узнать погоду", self)
        self.result_btn.setMinimumHeight(40)
        self.result_btn.setMinimumWidth(150)

        my_icon = QIcon("icons/search.png")
        self.result_btn.setIconSize(QSize(20, 20))

        self.result_btn.setIcon(my_icon)
        self.result_btn.setIconSize(QSize(20, 20))


        self.result_btn.setStyleSheet(ButtonStyle.weather_btn)




        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.result_btn)
        btn_layout.addStretch()



        #
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(lineEdit_WriteCity)
        h_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addStretch(3)
        main_layout.addLayout(h_layout)
        main_layout.addSpacing(5)
        main_layout.addLayout(btn_layout)
        main_layout.addStretch(1)

        self.setLayout(main_layout)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
