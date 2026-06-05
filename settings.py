import os

SETTINGS_FILE = "settings.txt"

def save_last_city(city):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        f.write(f"last_city={city}")

def load_last_city():
    if not os.path.exists(SETTINGS_FILE):
        return None
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("last_city="):
                return line.strip().split("=", 1)[1]
    return None


def save_theme(theme):
    lines = []
    city = None

    # Читаем существующий файл
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("last_city="):
                    city = line.strip().split("=", 1)[1]
                else:
                    lines.append(line)

    # Перезаписываем файл
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        if city:
            f.write(f"last_city={city}\n")
        f.write(f"theme={theme}\n")
        for line in lines:
            f.write(line)


def load_theme():
    if not os.path.exists(SETTINGS_FILE):
        return None
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("theme="):
                return line.strip().split("=", 1)[1]
    return None