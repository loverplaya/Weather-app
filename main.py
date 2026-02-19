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

        # Поле ввода города основное
        search_field = QLineEdit(self)
        search_field.setPlaceholderText("Введите местоположение")
        search_field.setMinimumWidth(300)
        search_field.setMinimumHeight(35)
        search_field.setStyleSheet(LineEdit_Style.writeCity_LineEdit)

        # Поле ввода города верхнее
        self.search_field_up = QLineEdit(self)
        self.search_field_up.setPlaceholderText("Введите местоположение")
        self.search_field_up.setMinimumWidth(224)
        self.search_field_up.setMinimumHeight(37)
        self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
        self.search_field_up.move(self.width() - 225,5)


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
        h_layout.addWidget(search_field)
        h_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addStretch(3)
        main_layout.addLayout(h_layout)
        main_layout.addSpacing(5)
        main_layout.addLayout(btn_layout)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

    # Обновление позиции поля при изменении размера окна
    def resizeEvent(self, event):
        self.search_field_up.move(self.width() - 225,5)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
