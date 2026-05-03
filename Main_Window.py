from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QStackedWidget, QMessageBox)
from PyQt6.QtGui import QIcon
from background import background
from location import get_city_by_ip
from main_screen import main_screen
from weather_screen import weather_screen
from weather_API import show_weather
from styles import ButtonStyle, LineEdit_Style, MessageStyle
from utils import show_message, resource_path
from favorites import add_favorite
from favorites_screen import FavoritesScreen
from weather_API import show_weather

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

        # Создаём экраны
        self.main_screen = main_screen(self)
        self.weather_screen = weather_screen(self)
        self.fav_screen = FavoritesScreen(self)

        # Погода по IP при запуске
        city = get_city_by_ip()
        if city:
            result = show_weather(city)
            if result and "main" in result and "temp" in result["main"]:
                temp = result['main']['temp']
                humidity = result['main']['humidity']
                wind = result['wind']['speed']
                desc = result['weather'][0]['description'] if 'weather' in result else ''

                # Формируем текст
                text = f"<b>{city}</b><br>🌡️ {temp:.1f}°C  💧 {humidity}%  🌬️ {wind:.1f} м/с<br>📖 {desc}"
                self.main_screen.weather_summary.setText(text)
            else:
                self.main_screen.weather_summary.setText("Не удалось загрузить погоду")
        else:
            self.main_screen.weather_summary.setText("Город не определён")

        # Добавляем в стек
        self.stacked.addWidget(self.main_screen)  # индекс 0
        self.stacked.addWidget(self.weather_screen)  # индекс 1
        self.stacked.addWidget(self.fav_screen) # индекс 2

        self.main_screen.fav_list_btn.clicked.connect(self.go_to_favorites)
        self.fav_screen.back_btn.clicked.connect(self.go_back)
        self.main_screen.location_btn.clicked.connect(self.on_location_clicked)

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

    def go_to_favorites(self):
        self.fav_screen.refresh_list(self.search_from_fav)
        self.stacked.setCurrentIndex(2)

    # Метод для поиска погоды прямо из списка избранного
    def search_from_fav(self, city_name):
        self.on_search_clicked(city=city_name)

    def on_search_clicked(self, city=None):
        # Если город не передан напрямую, берем его из полей ввода
        if not city:
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

        # Если всё хорошо  обновляем экран погоды
        if "main" in result and "temp" in result["main"]:
            temp = result['main']['temp']
            humidity = result['main']['humidity']
            pressure = result['main']['pressure']
            wind = result['wind']['speed']
            desc = result['weather'][0]['description'] if 'weather' in result else ''
            city_name = result.get("name", city)
            self.load_forecast(city_name)

            self.weather_screen.set_weather(city_name, temp, humidity, wind, pressure, desc)
            self.stacked.setCurrentIndex(1)
        else:
            show_message(self, "Ошибка", "Не удалось получить данные о погоде", "error")


    def add_to_favorites(self):
        city = self.weather_screen.city_label.text()
        if city and city != "Город":
            if add_favorite(city):
                print(f"Добавлено в файл: {city}")
                self.weather_screen.fav_btn.setStyleSheet(ButtonStyle.fav_btn_active)
                show_message(self, "Избранное", f"Город '{city}' добавлен", "info")
            else:
                show_message(self, "Инфо", "Город уже есть в избранном", "info")
        else:
            show_message(self, "Ошибка", "Нет города для добавления", "error")

    def toggle_theme(self):
        if self.bg.current_theme == "light":
            self.bg.set_theme("dark")
            self.apply_theme_to_screen("dark")
        else:
            self.bg.set_theme("light")
            self.apply_theme_to_screen("light")

    def on_location_clicked(self):
        self.update_weather_by_ip_on_main()

    def apply_theme_to_screen(self, theme):
        if hasattr(self.main_screen, 'apply_theme'):
            self.main_screen.apply_theme(theme)
        if hasattr(self.weather_screen, 'apply_theme'):
            self.weather_screen.apply_theme(theme)
        if hasattr(self.fav_screen, 'apply_theme'):
            self.fav_screen.apply_theme(theme)

    def update_weather_by_ip_on_main(self):
        city = get_city_by_ip()
        if city:
            result = show_weather(city)
            if result and "main" in result and "temp" in result["main"]:
                temp = result['main']['temp']
                humidity = result['main']['humidity']
                wind = result['wind']['speed']
                desc = result['weather'][0]['description'] if 'weather' in result else ''

                text = f"<b>{city}</b><br>🌡️ {temp:.1f}°C  💧 {humidity}%  🌬️ {wind:.1f} м/с<br>📖 {desc}"
                self.main_screen.weather_summary.setText(text)
            else:
                self.main_screen.weather_summary.setText("Не удалось загрузить погоду")
        else:
            self.main_screen.weather_summary.setText("Город не определён")

    def load_forecast(self, city):
        from weather_API import get_forecast
        forecast = get_forecast(city)
        self.weather_screen.display_forecast(forecast)

    def go_back(self):
        self.main_screen.search_field_center.clear()
        self.weather_screen.search_field_up.clear()
        self.weather_screen.fav_btn.setStyleSheet(ButtonStyle.weather_btn)
        self.stacked.setCurrentIndex(0)