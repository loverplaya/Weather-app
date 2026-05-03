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

        # Прогноз на 5 дней
        self.forecast_title = QLabel("Прогноз на 5 дней")
        self.forecast_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.forecast_title.setStyleSheet("font-size: 20px; font-weight: bold; color: white; margin-top: 20px;")
        self.forecast_title.setVisible(False)
        main_layout.addWidget(self.forecast_title)

        self.forecast_layout = QHBoxLayout()
        self.forecast_layout.setSpacing(15)
        main_layout.addLayout(self.forecast_layout)

        main_layout.addStretch(2)

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

    def display_forecast(self, forecast_data):
        while self.forecast_layout.count():
            item = self.forecast_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        if "error" in forecast_data or not forecast_data.get('list'):
            self.forecast_title.setVisible(False)
            return

        from datetime import datetime
        rus_days = {
            "Mon": "понедельник", "Tue": "вторник", "Wed": "среда", "Thu": "четверг",
            "Fri": "пятница", "Sat": "суббота", "Sun": "воскресенье"
        }

        days = {}
        for item in forecast_data.get('list', []):
            date = item['dt_txt'].split()[0]
            if date not in days:
                days[date] = item

        today = datetime.now().strftime("%Y-%m-%d")
        for date, item in days.items():
            if date == today:
                continue

            temp = item['main']['temp']
            desc = item['weather'][0]['description']
            icon_code = item['weather'][0]['icon']

            eng_day = datetime.strptime(date, "%Y-%m-%d").strftime("%a")
            day_name = rus_days.get(eng_day, eng_day)

            card = self._create_forecast_card(day_name, temp, desc, icon_code)
            self.forecast_layout.addWidget(card)

        if self.forecast_layout.count() > 0:
            self.forecast_title.setVisible(True)

    def _create_forecast_card(self, day_name, temp, desc, icon_code):
        card = QFrame()
        card.setMinimumWidth(160)
        card.setMinimumHeight(240)

        # Основная плашка
        card.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 0.25); 
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 25px;
            }
        """)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(10, 20, 10, 20)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #День недели
        day_label = QLabel(day_name.upper())
        day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        day_label.setStyleSheet("""
            font-size: 15px; 
            font-weight: 800; 
            color: #CCCCCC; 
            background: transparent; 
            border: none;
        """)

        #Иконка
        icon_label = QLabel(self._get_icon_emoji(icon_code))
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet("font-size: 45px; background: transparent; border: none;")

        #Температура
        temp_label = QLabel(f"{temp:.0f}°")
        temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        temp_label.setStyleSheet("""
            font-size: 38px; 
            font-weight: 700; 
            color: #FFFFFF; 
            background: transparent; 
            border: none;
        """)

        #Описание погоды
        desc_label = QLabel(desc.capitalize())
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc_label.setStyleSheet("""
            font-size: 15px; 
            color: #FFFFFF; 
            font-weight: 600;
            background: transparent; 
            border: none;
            padding: 0 5px;
        """)

        layout.addWidget(day_label)
        layout.addWidget(icon_label)
        layout.addWidget(temp_label)
        layout.addWidget(desc_label)

        return card

    def _get_icon_emoji(self, icon_code):
        if not icon_code:
            return "🌡️"
        code = icon_code[:2]
        icons = {
            "01": "☀️", "02": "⛅", "03": "☁️", "04": "☁️",
            "09": "🌧️", "10": "🌦️", "11": "⛈️", "13": "❄️", "50": "🌫️"
        }
        return icons.get(code, "🌡️")

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
