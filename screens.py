from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from styles import ButtonStyle, LineEdit_Style
import os

class main_screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        search_field = QLineEdit(self)
        search_field.setPlaceholderText("Введите местоположение")
        search_field.setMinimumWidth(300)
        search_field.setMinimumHeight(35)
        search_field.setStyleSheet(LineEdit_Style.writeCity_LineEdit)

        # Поле ввода города верхнее
        self.search_field_up = QLineEdit(self)
        self.search_field_up.setPlaceholderText("Введите местоположение")
        self.search_field_up.setFixedSize(224, 37)
        self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
        self.search_field_up.move(self.width() - 223, 5)

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

        if self.parent():
            self.update_position(self.parent().width())

    def update_position(self, parent_width):
        self.search_field_up.move(parent_width - 245, 5)