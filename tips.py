import os


class TipsManager:
    def __init__(self, tips_file="tips.txt"):
        self.tips_file = tips_file
        self.tips = self._load_tips()

    def _load_tips(self):
        tips = {
            'temperature': [],
            'conditions': {},
            'wind': [],
            'humidity': [],
            'default': "🌤️ Хорошего дня!"
        }

        if not os.path.exists(self.tips_file):
            return tips

        with open(self.tips_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                if '|' not in line:
                    continue

                key, tip = line.split('|', 1)
                key = key.strip()
                tip = tip.strip()

                if key.startswith('temperature_'):
                    parts = key.split(':')
                    if len(parts) == 2:
                        condition = parts[0].replace('temperature_', '')
                        try:
                            threshold = int(parts[1])
                            tips['temperature'].append({
                                'condition': condition,
                                'threshold': threshold,
                                'tip': tip
                            })
                        except ValueError:
                            pass
                elif key.startswith('wind_'):
                    parts = key.split(':')
                    if len(parts) == 2:
                        condition = parts[0].replace('wind_', '')
                        try:
                            threshold = int(parts[1])
                            tips['wind'].append({
                                'condition': condition,
                                'threshold': threshold,
                                'tip': tip
                            })
                        except ValueError:
                            pass
                elif key.startswith('humidity_'):
                    parts = key.split(':')
                    if len(parts) == 2:
                        condition = parts[0].replace('humidity_', '')
                        try:
                            threshold = int(parts[1])
                            tips['humidity'].append({
                                'condition': condition,
                                'threshold': threshold,
                                'tip': tip
                            })
                        except ValueError:
                            pass
                else:
                    if key == 'default':
                        tips['default'] = tip
                    else:
                        tips['conditions'][key] = tip

        return tips

    def get_tip(self, weather_data):
        if not weather_data or "error" in weather_data:
            return "Проверьте погоду, чтобы получить совет"

        temp = weather_data['main']['temp']
        desc = weather_data['weather'][0]['description'].lower()
        wind = weather_data['wind']['speed']
        humidity = weather_data['main']['humidity']

        # 1. Осадки и явления
        conditions_map = {
            'дождь': 'rain', 'ливень': 'rain', 'дождя': 'rain',
            'снег': 'snow', 'снега': 'snow',
            'гроза': 'thunderstorm', 'грозу': 'thunderstorm',
            'туман': 'fog', 'тумана': 'fog'
        }

        for keyword, condition in conditions_map.items():
            if keyword in desc:
                if condition in self.tips['conditions']:
                    return self.tips['conditions'][condition]

        # 2. Температура
        temp_tips = sorted(self.tips['temperature'], key=lambda x: abs(x['threshold']), reverse=True)
        for tip_info in temp_tips:
            if tip_info['condition'] == 'extreme_cold' and temp <= tip_info['threshold']:
                return tip_info['tip']
            elif tip_info['condition'] == 'cold' and temp <= tip_info['threshold']:
                return tip_info['tip']
            elif tip_info['condition'] == 'mild_cold' and temp <= tip_info['threshold']:
                return tip_info['tip']
            elif tip_info['condition'] == 'extreme_hot' and temp >= tip_info['threshold']:
                return tip_info['tip']
            elif tip_info['condition'] == 'hot' and temp >= tip_info['threshold']:
                return tip_info['tip']
            elif tip_info['condition'] == 'warm' and temp >= tip_info['threshold']:
                return tip_info['tip']

        # 3. Ветер
        for tip_info in self.tips['wind']:
            if tip_info['condition'] == 'strong' and wind >= tip_info['threshold']:
                return tip_info['tip']
            elif tip_info['condition'] == 'medium' and wind >= tip_info['threshold']:
                return tip_info['tip']

        # 4. Влажность
        for tip_info in self.tips['humidity']:
            if tip_info['condition'] == 'high' and humidity >= tip_info['threshold']:
                return tip_info['tip']
            elif tip_info['condition'] == 'low' and humidity <= tip_info['threshold']:
                return tip_info['tip']

        return self.tips['default']