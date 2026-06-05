import requests

def save_last_city(city):
    with open("last_city.txt", "w", encoding="utf-8") as f:
        f.write(city)

def load_last_city():
    try:
        with open("last_city.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except:
        return None

def get_location(ip=None):
    try:
        if ip is None:
            url = 'http://ipwho.is/?lang=ru'
        else:
            url = f'http://ipwho.is/{ip}?lang=ru'

        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()

            if data.get('success') != False:
                city = data.get('city')

                if city:
                    save_last_city(city)

                return {'city': city}

    except Exception as e:
        print("Location error:", e)

    return None

DEFAULT_CITY = "Киров"

def get_city_by_ip():
    location = get_location()

    if location and location.get('city'):
        city = location['city']
        save_last_city(city)
        return city

    cached = load_last_city()
    if cached:
        return cached

    return DEFAULT_CITY