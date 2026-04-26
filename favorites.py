import os

FILE_PATH = "favorites.txt"

def add_favorite(city):
    # какие города уже добавлены, чтобы не дублировать
    cities = get_favorites()
    if city not in cities:
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(city + "\n")
        return True
    return False

def get_favorites():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
