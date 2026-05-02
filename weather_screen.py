from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QFrame, QScrollArea
from PyQt6.QtCore import Qt
from styles import ButtonStyle, LineEdit_Style

class weather_screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 30, 50, 50)
        main_layout.setSpacing(0)

        # ВЕРХНЯЯ ПАНЕЛЬ
        top_panel = QHBoxLayout()
        top_panel.setContentsMargins(0, 0, 10, 0)

        top_panel.addStretch()

        self.search_field_up = QLineEdit()
        self.search_field_up.setPlaceholderText("Поиск...")

        self.search_field_up.setFixedWidth(200)
        self.search_field_up.setMinimumHeight(35)

        self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
        top_panel.addWidget(self.search_field_up)

        main_layout.addLayout(top_panel)

        main_layout.addStretch(1)

        # Название города
        self.city_label = QLabel("Город")
        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_label.setStyleSheet("font-size: 54px; font-weight: 800; color: white; background: none;")
        main_layout.addWidget(self.city_label)

        # Температура
        self.temp_label = QLabel("--°")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_label.setStyleSheet(
            "font-size: 140px; font-weight: 200; color: white; margin: -10px 0; background: none;")
        main_layout.addWidget(self.temp_label)

        # Описание
        self.desc_label = QLabel("--")
        self.desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.desc_label.setStyleSheet("font-size: 24px; color: rgba(255, 255, 255, 0.7); background: none;")
        main_layout.addWidget(self.desc_label)

        main_layout.addSpacing(60)

        details_layout = QHBoxLayout()

        self.humidity_widget = self._create_detail_widget("💧", "ВЛАЖНОСТЬ", "--%")
        self.wind_widget = self._create_detail_widget("🌬️", "ВЕТЕР", "-- м/с")
        self.pressure_widget = self._create_detail_widget("📊", "ДАВЛЕНИЕ", "-- гПа")

        def create_divider():
            line = QFrame()
            line.setFrameShape(QFrame.Shape.VLine)
            line.setFixedHeight(45)
            line.setStyleSheet("background-color: rgba(255, 255, 255, 0.2); border: none;")
            return line

        details_layout.addStretch()
        details_layout.addWidget(self.humidity_widget)
        details_layout.addSpacing(40)
        details_layout.addWidget(create_divider())
        details_layout.addSpacing(40)
        details_layout.addWidget(self.wind_widget)
        details_layout.addSpacing(40)
        details_layout.addWidget(create_divider())
        details_layout.addSpacing(40)
        details_layout.addWidget(self.pressure_widget)
        details_layout.addStretch()

        main_layout.addLayout(details_layout)

        main_layout.addStretch(2)

        # Кнопки управления
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(20)
        buttons_layout.addStretch()

        self.fav_btn = QPushButton("⭐ В избранное")
        self.fav_btn.setFixedSize(200, 50)
        self.fav_btn.setStyleSheet(ButtonStyle.weather_btn)

        self.back_btn = QPushButton("← На главную")
        self.back_btn.setFixedSize(200, 50)
        self.back_btn.setStyleSheet(ButtonStyle.weather_btn)

        buttons_layout.addWidget(self.fav_btn)
        buttons_layout.addWidget(self.back_btn)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def _create_detail_widget(self, icon, title, value):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(5)

        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 28px;")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel(title)
        title_label.setStyleSheet(
            "font-size: 12px; color: rgba(255, 255, 255, 0.5); font-weight: 700; letter-spacing: 1px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        value_label = QLabel(value)
        value_label.setStyleSheet("font-size: 22px; font-weight: 600; color: white;")
        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(icon_label)
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        return widget

    def set_weather(self, city, temp, humidity, wind, pressure, description):
        self.city_label.setText(city)
        self.temp_label.setText(f"{temp:.0f}°")
        self.desc_label.setText(description.capitalize())
        self._set_detail_value(self.humidity_widget, f"{humidity}%")
        self._set_detail_value(self.wind_widget, f"{wind:.1f} м/с")
        self._set_detail_value(self.pressure_widget, f"{pressure} гПа")

    def _set_detail_value(self, widget, value):
        layout = widget.layout()
        if layout:
            value_label = layout.itemAt(2).widget()
            if value_label:
                value_label.setText(value)

    def apply_theme(self, theme):
        if theme == "dark":
            self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit_dark)
        else:
            self.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
