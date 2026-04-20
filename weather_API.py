import requests
from urllib.parse import quote

def show_weather(city_name):
    if not city_name:
        return None

    city_name = city_name.strip()
    encoded_city = quote(city_name)

    API_KEY = "8bdb15b546a790008f694f2cd2db2e7e"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={API_KEY}&units=metric&lang=ru"

    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None