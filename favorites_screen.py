from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea, QHBoxLayout
from PyQt6.QtCore import Qt, QSize
from styles import ButtonStyle
from favorites import get_favorites
from PyQt6.QtGui import QIcon
from utils import resource_path


class FavoritesScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_theme = "light"
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
        self._on_city_click = on_city_click
        # Очищаем старые кнопки и растяжки
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        # загрузка города из файла
        cities = get_favorites()

        if self.current_theme == "dark":
            city_style = ButtonStyle.weather_btn_dark
            del_style = ButtonStyle.del_btn_dark
        else:
            city_style = ButtonStyle.weather_btn
            del_style = ButtonStyle.del_btn

        for city in cities:
            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)
            item_layout.setContentsMargins(0, 0, 0, 0)
            item_layout.setSpacing(10)

            city_btn = QPushButton(city)
            city_btn.setStyleSheet(city_style)
            city_btn.clicked.connect(lambda checked, c=city: on_city_click(c))
            item_layout.addWidget(city_btn)

            del_btn = QPushButton()
            del_btn.setFixedSize(40, 40)
            del_btn.setStyleSheet(del_style)
            icon_path = resource_path("icons/delete.png")
            del_btn.setIcon(QIcon(icon_path))
            del_btn.setIconSize(QSize(22, 22))
            del_btn.setToolTip("Удалить город")
            del_btn.clicked.connect(lambda checked, c=city: self.remove_favorite(c, on_city_click))
            item_layout.addWidget(del_btn)
            self.scroll_layout.addWidget(item_widget)

        self.scroll_layout.addStretch()

    def remove_favorite(self, city, on_city_click):
        from favorites import get_favorites, save_favorites
        cities = get_favorites()
        if city in cities:
            cities.remove(city)
            save_favorites(cities)
            self.refresh_list(on_city_click)

    def apply_theme(self, theme):
        self.current_theme = theme
        if theme == "dark":
            self.title.setStyleSheet("font-size: 24px; color: #cccccc; font-weight: bold;")
            self.back_btn.setStyleSheet(ButtonStyle.weather_btn_dark)
            del_style = ButtonStyle.del_btn_dark
            city_style = ButtonStyle.weather_btn_dark
        else:
            self.title.setStyleSheet("font-size: 24px; color: white; font-weight: bold;")
            self.back_btn.setStyleSheet(ButtonStyle.weather_btn)
            del_style = ButtonStyle.del_btn
            city_style = ButtonStyle.weather_btn

        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                if hasattr(widget, 'layout') and widget.layout():
                    layout = widget.layout()
                    if layout.count() >= 2:
                        city_btn = layout.itemAt(0).widget()
                        del_btn = layout.itemAt(1).widget()
                        if city_btn:
                            city_btn.setStyleSheet(city_style)
                        if del_btn:
                            del_btn.setStyleSheet(del_style)
