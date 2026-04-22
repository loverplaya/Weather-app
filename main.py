import sys
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QStackedWidget, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from background import background
from screens import main_screen, weather_screen
from weather_API import show_weather
from styles import ButtonStyle
from styles import LineEdit_Style

# чтобы при компиляции были видны иконки
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(600, 200, 800, 600)
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

        # Создаём экраны
        self.main_screen = main_screen(self)
        self.weather_screen = weather_screen(self)

        # Добавляем в стек
        self.stacked.addWidget(self.main_screen)  # индекс 0
        self.stacked.addWidget(self.weather_screen)  # индекс 1

        # Главный layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked)
        self.setLayout(main_layout)

        # Подключаем кнопки
        self.main_screen.result_btn.clicked.connect(self.on_search_clicked)
        self.main_screen.search_field_center.returnPressed.connect(self.on_search_clicked)
        self.weather_screen.back_btn.clicked.connect(self.go_back)

    def on_search_clicked(self):
        city = self.main_screen.search_field_center.text()
        if not city:
            QMessageBox.warning(self, "Ошибка", "Введите название города")
            return

        weather_data = show_weather(city)
        if weather_data:
            temp = weather_data['main']['temp']
            self.weather_screen.set_weather(city, temp)
            self.stacked.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Ошибка", f"Город '{city}' не найден")

    def go_back(self):
        self.stacked.setCurrentIndex(0)

    def toggle_theme(self):
        if self.bg.current_theme == "light":
            self.bg.set_theme("dark")
            self.apply_theme_to_screen("dark")
        else:
            self.bg.set_theme("light")
            self.apply_theme_to_screen("light")

    def apply_theme_to_screen(self, theme):
        if theme == "dark":
            # поля ввода
            self.main_screen.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit_dark)
            self.main_screen.search_field_center.setStyleSheet(LineEdit_Style.writeCity_LineEdit_dark)
            # кнопки
            self.main_screen.result_btn.setStyleSheet(ButtonStyle.weather_btn_dark)
            self.weather_screen.back_btn.setStyleSheet(ButtonStyle.back_btn_dark)
        else:
            # поля ввода
            self.main_screen.search_field_up.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
            self.main_screen.search_field_center.setStyleSheet(LineEdit_Style.writeCity_LineEdit)
            # кнопки
            self.main_screen.result_btn.setStyleSheet(ButtonStyle.weather_btn)
            self.weather_screen.back_btn.setStyleSheet(ButtonStyle.back_btn)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())