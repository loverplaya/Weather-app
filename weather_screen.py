from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from styles import ButtonStyle, LineEdit_Style
from utils import resource_path # Импортируем из utils

class weather_screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        # верхняя панель
        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0, 5, 10, 0)
        self.top_layout.addStretch()

        self.search_field_up = QLineEdit()
        self.search_field_up.setPlaceholderText("Введите местоположение")
        self.search_field_up.setMinimumWidth(180)
        self.search_field_up.setMaximumWidth(300)
        self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
        self.top_layout.addWidget(self.search_field_up)

        layout = QVBoxLayout()

        self.city_label = QLabel("Город")
        self.city_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.temp_label = QLabel("--°C")
        self.temp_label.setStyleSheet("font-size: 48px; font-weight: bold; color: white;")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fav_btn = QPushButton("")
        self.fav_btn.setFixedSize(50, 50)
        self.fav_btn.setIcon(QIcon(resource_path("icons/star.png")))
        self.fav_btn.setIconSize(QSize(32, 32))
        self.fav_btn.setStyleSheet(ButtonStyle.fav_btn)
        self.fav_btn.setToolTip("Добавить в избранное")

        self.back_btn = QPushButton("← Назад")
        self.back_btn.setMinimumHeight(40)
        self.back_btn.setMinimumWidth(150)
        self.back_btn.setStyleSheet(ButtonStyle.weather_btn)

        layout.addLayout(self.top_layout)
        layout.addStretch()
        layout.addWidget(self.city_label)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.fav_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.back_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        self.setLayout(layout)

    def set_weather(self, city, temp):
        self.city_label.setText(city)
        self.temp_label.setText(f"{temp:.1f}°C")

    def apply_theme(self, theme):
        if theme == "dark":
            self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit_dark)
            self.city_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #cccccc;")
            self.temp_label.setStyleSheet("font-size: 48px; font-weight: bold; color: #cccccc;")
            self.fav_btn.setStyleSheet(ButtonStyle.fav_btn + "background-color: rgba(0,0,0,0.2);")
        else:
            self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
            self.city_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
            self.temp_label.setStyleSheet("font-size: 48px; font-weight: bold; color: white;")
            self.fav_btn.setStyleSheet(ButtonStyle.fav_btn)
