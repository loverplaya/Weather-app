from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
from PyQt6.QtCore import Qt
from styles import ButtonStyle
from favorites import get_favorites


class FavoritesScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.layout = QVBoxLayout(self)

        self.title = QLabel("Избранные города")
        self.title.setStyleSheet("font-size: 24px; color: white; font-weight: bold;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("background: transparent; border: none;")

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll.setWidget(self.scroll_content)

        self.layout.addWidget(self.scroll)

        # Кнопка назад
        self.back_btn = QPushButton("← Назад")
        self.back_btn.setStyleSheet(ButtonStyle.weather_btn)
        self.layout.addWidget(self.back_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def refresh_list(self, on_city_click):
        # Очищаем старые кнопки и растяжки
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        # загрузка города из файла
        cities = get_favorites()

        for city in cities:
            btn = QPushButton(city)
            btn.setStyleSheet(ButtonStyle.weather_btn)
            # При нажатии вызывается поиск погоды для этого города
            btn.clicked.connect(lambda checked, c=city: on_city_click(c))
            self.scroll_layout.addWidget(btn)

        self.scroll_layout.addStretch()

    def apply_theme(self, theme):
        if theme == "dark":
            self.title.setStyleSheet("font-size: 24px; color: #cccccc; font-weight: bold;")
            self.back_btn.setStyleSheet(ButtonStyle.weather_btn_dark)
        else:
            self.title.setStyleSheet("font-size: 24px; color: white; font-weight: bold;")
            self.back_btn.setStyleSheet(ButtonStyle.weather_btn)

        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                if isinstance(widget, QPushButton) and widget != self.back_btn:
                    style = ButtonStyle.weather_btn_dark if theme == "dark" else ButtonStyle.weather_btn
                    widget.setStyleSheet(style)
