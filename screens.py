from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont
from styles import ButtonStyle, LineEdit_Style
import os
import sys

# чтобы при компиляции были видны иконки
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class main_screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        # ВЕРХНЯЯ ПАНЕЛЬ
        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0, 5, 10, 0)
        self.top_layout.addStretch()

        self.change_theme = QPushButton()
        self.change_theme.setIcon(QIcon(resource_path("icons/change_theme1.png")))
        self.change_theme.setIconSize(QSize(20, 20))
        self.change_theme.setFixedSize(37, 37)
        self.change_theme.setStyleSheet("border-radius: 10px; background-color: rgba(255,255,255,0.2);")
        self.change_theme.clicked.connect(self.on_theme_clicked)

        self.search_field_up = QLineEdit()
        self.search_field_up.setPlaceholderText("Введите местоположение")
        self.search_field_up.setMinimumWidth(180)
        self.search_field_up.setMaximumWidth(300)
        self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)

        self.top_layout.addWidget(self.change_theme)
        self.top_layout.addWidget(self.search_field_up)

        # Центральная часть
        self.search_field_center = QLineEdit()
        self.search_field_center.setPlaceholderText("Введите местоположение")
        self.search_field_center.setMinimumWidth(300)
        self.search_field_center.setMinimumHeight(35)
        self.search_field_center.setStyleSheet(LineEdit_Style.writeCity_LineEdit)

        self.result_btn = QPushButton(" Узнать погоду")
        self.result_btn.setMinimumHeight(40)
        self.result_btn.setMinimumWidth(150)
        self.result_btn.setIcon(QIcon(resource_path("icons/search.png")))
        self.result_btn.setIconSize(QSize(20, 20))
        self.result_btn.setStyleSheet(ButtonStyle.weather_btn)

        # Сборка макетов
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.search_field_center)
        h_layout.addStretch()

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.result_btn)
        btn_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.top_layout)
        main_layout.addStretch(3)
        main_layout.addLayout(h_layout)
        main_layout.addSpacing(5)
        main_layout.addLayout(btn_layout)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

    def on_theme_clicked(self):
        # Ищем родителя с методом toggle_theme (поднимаемся выше)
        parent = self.parent()
        while parent:
            if hasattr(parent, 'toggle_theme'):
                parent.toggle_theme()
                return
            parent = parent.parent()

    def update_position(self, width):
        pass


class weather_screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        self.city_label = QLabel("Город")
        self.city_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.temp_label = QLabel("--°C")
        self.temp_label.setStyleSheet("font-size: 48px; font-weight: bold; color: white;")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.back_btn = QPushButton("← Назад")
        self.back_btn.setMinimumHeight(40)
        self.back_btn.setMinimumWidth(150)
        self.back_btn.setStyleSheet(ButtonStyle.weather_btn)

        layout.addStretch()
        layout.addWidget(self.city_label)
        layout.addWidget(self.temp_label)
        layout.addStretch()
        layout.addWidget(self.back_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        self.setLayout(layout)

    def set_weather(self, city, temp):
        self.city_label.setText(city)
        self.temp_label.setText(f"{temp:.1f}°C")

    def apply_theme(self, theme):
        if theme == "dark":
            self.back_btn.setStyleSheet(ButtonStyle.back_btn_dark)
        else:
            self.back_btn.setStyleSheet(ButtonStyle.back_btn)