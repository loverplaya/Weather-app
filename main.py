import sys
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QStackedWidget, QMessageBox)
from PyQt6.QtGui import QIcon
from background import background
from screens import main_screen
from weather_screen import weather_screen
from weather_API import show_weather
from styles import ButtonStyle, LineEdit_Style, MessageStyle
from utils import show_message, resource_path

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(600, 200, 1366, 768)
        self.setWindowTitle("Прогноз погоды")
        self.setWindowIcon(QIcon(resource_path("icons/app_icon.ico")))
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # Фон
        self.bg = background(self)
        self.bg.apply_gradient()

        # Стек экранов
        self.stacked = QStackedWidget()

        # Создаём экраны (ТОЛЬКО ОДИН РАЗ)
        self.main_screen = main_screen(self)
        self.weather_screen = weather_screen(self)

        # Добавляем в стек
        self.stacked.addWidget(self.main_screen)  # индекс 0
        self.stacked.addWidget(self.weather_screen)  # индекс 1

        try:
            self.main_screen.change_theme.clicked.disconnect()
        except:
            pass
        self.main_screen.change_theme.clicked.connect(self.toggle_theme)

        # Главный layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked)
        self.setLayout(main_layout)

        # Подключение кнопок (главный экран)
        self.main_screen.result_btn.clicked.connect(self.on_search_clicked)
        self.main_screen.search_field_center.returnPressed.connect(self.on_search_clicked)
        self.weather_screen.back_btn.clicked.connect(self.go_back)

        # Подключение кнопок (экран погоды)
        self.weather_screen.fav_btn.clicked.connect(self.add_to_favorites)
        self.weather_screen.search_field_up.returnPressed.connect(self.on_search_clicked)

    def on_search_clicked(self):
        if self.stacked.currentIndex() == 0:
            city = self.main_screen.search_field_center.text()
        else:
            city = self.weather_screen.search_field_up.text()

        if not city:
            show_message(self, "Ошибка", "Введите название города", "error")
            return

        result = show_weather(city)

        if result is None:
            show_message(self, "Ошибка", "Неизвестная ошибка", "error")
            return

        # Если пришёл словарь с ошибкой
        if "error" in result:
            error = result["error"]
            if error == "not_found":
                show_message(self, "Ошибка", f"Город '{city}' не найден", "error")
            elif error == "no_internet":
                show_message(self, "Ошибка", "Нет подключения к интернету", "error")
            elif error == "timeout":
                show_message(self, "Ошибка", "Сервер не отвечает. Попробуйте позже", "error")
            else:
                show_message(self, "Ошибка", f"Ошибка API: {result.get('code', 'unknown')}", "error")
            return

        # Если всё хорошо
        if "main" in result and "temp" in result["main"]:
            temp = result['main']['temp']
            self.weather_screen.set_weather(city, temp)
            self.stacked.setCurrentIndex(1)
        else:
            show_message(self, "Ошибка", "Не удалось получить данные о погоде", "error")

    def go_back(self):
        self.stacked.setCurrentIndex(0)

    def add_to_favorites(self):
        city = self.weather_screen.city_label.text()
        if city and city != "Город":
            print(f"Добавлено в избранное: {city}")
            # временно меняется стиль кнопки
            self.weather_screen.fav_btn.setStyleSheet(ButtonStyle.fav_btn_active)
            show_message(self, "Избранное", f"Город '{city}' добавлен в избранное", "info")
        else:
            show_message(self, "Ошибка", "Нет города для добавления", "error")

    def toggle_theme(self):
        if self.bg.current_theme == "light":
            self.bg.set_theme("dark")
            self.apply_theme_to_screen("dark")
        else:
            self.bg.set_theme("light")
            self.apply_theme_to_screen("light")

    def apply_theme_to_screen(self, theme):
        if hasattr(self.main_screen, 'apply_theme'):
            self.main_screen.apply_theme(theme)
        if hasattr(self.weather_screen, 'apply_theme'):
            self.weather_screen.apply_theme(theme)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())