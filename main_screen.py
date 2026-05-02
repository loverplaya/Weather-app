from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from styles import ButtonStyle, LineEdit_Style
from utils import resource_path

class main_screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        # Верхняя часть
        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0, 5, 10, 0)
        self.top_layout.addStretch()

        self.change_theme = QPushButton()
        self.change_theme.setIcon(QIcon(resource_path("icons/change_theme1.png")))
        self.change_theme.setIconSize(QSize(20, 20))
        self.change_theme.setFixedSize(37, 37)
        self.change_theme.setStyleSheet("border-radius: 10px; background-color: rgba(255,255,255,0.2);")


        self.search_field_up = QLineEdit()
        self.search_field_up.setPlaceholderText("Введите местоположение")
        self.search_field_up.setMinimumWidth(180)
        self.search_field_up.setMaximumWidth(300)
        self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)

        self.fav_list_btn = QPushButton()
        self.fav_list_btn.setIcon(QIcon(resource_path("icons/star.png")))
        self.fav_list_btn.setIconSize(QSize(20, 20))
        self.fav_list_btn.setFixedSize(37, 37)
        self.fav_list_btn.setStyleSheet("border-radius: 10px; background-color: rgba(255,255,255,0.2);")

        self.location_btn = QPushButton("🔄")
        self.location_btn.setFixedSize(37, 37)
        self.location_btn.setStyleSheet("border-radius: 10px; background-color: rgba(255,255,255,0.2);")

        self.top_layout.addWidget(self.change_theme)
        self.top_layout.addWidget(self.fav_list_btn)
        self.top_layout.addWidget(self.location_btn)
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

        # Краткая информация о погоде по IP
        self.weather_summary = QLabel("Погода загружается...")
        self.weather_summary.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.weather_summary.setMaximumWidth(500)
        self.weather_summary.setMinimumWidth(320)
        self.weather_summary.setMinimumHeight(100)
        self.weather_summary.setStyleSheet("""
            QLabel {
                font-size: 16px; 
                color: white; 
                background-color: rgba(0, 0, 0, 0.4); 
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 25px; 
                padding: 20px 25px;
            }
        """)
        self.weather_summary.setWordWrap(True)
        self.weather_summary.setMinimumHeight(80)

        # Сборка макетов
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.search_field_center)
        h_layout.addStretch()

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.result_btn)
        btn_layout.addStretch()

        weather_layout = QHBoxLayout()
        weather_layout.addStretch()
        weather_layout.addWidget(self.weather_summary)
        weather_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.top_layout)

        main_layout.addStretch(1)

        main_layout.addLayout(weather_layout)
        main_layout.addSpacing(10)
        main_layout.addLayout(h_layout)
        main_layout.addSpacing(10)
        main_layout.addLayout(btn_layout)

        main_layout.addStretch(1)

        self.setLayout(main_layout)

    def apply_theme(self, theme):
        if theme == "dark":
            self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit_dark)
            self.search_field_center.setStyleSheet(LineEdit_Style.writeCity_LineEdit_dark)
            self.result_btn.setStyleSheet(ButtonStyle.weather_btn_dark)
            self.change_theme.setStyleSheet("border-radius: 10px; background-color: rgba(0,0,0,0.3);")
            self.fav_list_btn.setStyleSheet("border-radius: 10px; background-color: rgba(0,0,0,0.3);")
            self.location_btn.setStyleSheet("border-radius: 10px; background-color: rgba(0,0,0,0.3);")
        else:
            self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
            self.search_field_center.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
            self.result_btn.setStyleSheet(ButtonStyle.weather_btn)
            self.change_theme.setStyleSheet("border-radius: 10px; background-color: rgba(255,255,255,0.2);")
            self.fav_list_btn.setStyleSheet("border-radius: 10px; background-color: rgba(255,255,255,0.2);")
            self.location_btn.setStyleSheet("border-radius: 10px; background-color: rgba(255,255,255,0.2);")


