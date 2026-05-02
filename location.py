import requests

def get_location(ip=None):
    try:
        if ip is None:
            url = 'https://ipwho.is/?lang=ru'
        else:
            url = f'https://ipwho.is/{ip}?lang=ru'

        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if not data.get('success') == False:
                return {
                    'city': data.get('city')
                }
    except Exception as e:
        pass

    return None

def get_city_by_ip():
    location = get_location()
    return location['city'] if location else None