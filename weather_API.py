import requests
from urllib.parse import quote
from location import get_location, get_city_by_ip

def show_weather(city_name):
    if not city_name:
        return {"error": "empty"}

    city_name = city_name.strip()
    encoded_city = quote(city_name)

    API_KEY = "8bdb15b546a790008f694f2cd2db2e7e"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={API_KEY}&units=metric&lang=ru"

    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"error": "not_found"}
        else:
            return {"error": "api_error", "code": response.status_code}
    except requests.exceptions.ConnectionError:
        return {"error": "no_internet"}
    except requests.exceptions.Timeout:
        return {"error": "timeout"}
    except:
        return {"error": "unknown"}

def show_weather_by_ip():
    city = get_city_by_ip()
    if not city:
        return {"error": "no_city_by_ip"}
    return show_weather(city)

def get_forecast(city_name):
    """Получает прогноз на 5 дней (каждые 3 часа)"""
    if not city_name:
        return {"error": "empty"}

    city_name = city_name.strip()
    encoded_city = quote(city_name)

    API_KEY = "8bdb15b546a790008f694f2cd2db2e7e"
    URL = f"https://api.openweathermap.org/data/2.5/forecast?q={encoded_city}&appid={API_KEY}&units=metric&lang=ru"

    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"error": "not_found"}
        else:
            return {"error": "api_error", "code": response.status_code}
    except requests.exceptions.ConnectionError:
        return {"error": "no_internet"}
    except requests.exceptions.Timeout:
        return {"error": "timeout"}
    except:
        return {"error": "unknown"}


def get_weather_tip(weather_data):
    """Возвращает совет на основе погодных данных"""
    if not weather_data or "error" in weather_data:
        return "Проверьте погоду, чтобы получить совет"

    temp = weather_data['main']['temp']
    desc = weather_data['weather'][0]['description'].lower()
    wind = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']

    # Советы по температуре
    if temp < -20:
        return "🥶 Экстремально холодно! Оставайтесь дома, одевайтесь максимально тепло."
    elif temp < -10:
        return "🧣 Очень холодно! Не забудьте тёплую куртку, шапку и перчатки."
    elif temp < 0:
        return "🧥 Холодно! Наденьте пуховик и будьте осторожны на гололёде."
    elif temp > 35:
        return "🔥 Экстремальная жара! Не выходите на солнце, пейте больше воды."
    elif temp > 30:
        return "🥵 Жарко! Пейте воду, носите светлую одежду, используйте крем от загара."
    elif temp > 25:
        return "☀️ Тепло! Хороший день для прогулки, но не забывайте про воду."

    # Советы по осадкам
    if 'дождь' in desc or 'ливень' in desc:
        return "☔ Не забудьте зонт! Ожидается дождь."
    elif 'снег' in desc:
        return "❄️ Идёт снег! Одевайтесь теплее, дороги могут быть скользкими."
    elif 'гроза' in desc:
        return "⚡ Гроза! Лучше остаться дома и отключить электроприборы."
    elif 'туман' in desc:
        return "🌫️ Туман! Будьте осторожны на дорогах, включите ближний свет."

    # Советы по ветру
    if wind > 15:
        return "💨 Очень сильный ветер! Закрепите вещи на балконе, будьте осторожны."
    elif wind > 10:
        return "🍃 Сильный ветер! Застегните куртку, зонт может вывернуть."

    # Советы по влажности
    if humidity > 80:
        return "💧 Высокая влажность. Может быть душно, проветрите помещение."
    elif humidity < 20:
        return "🏜️ Низкая влажность. Пейте больше воды, увлажняйте воздух."

    # Совет по умолчанию
    return f"🌤️ {desc.capitalize()}. Хорошего дня!"