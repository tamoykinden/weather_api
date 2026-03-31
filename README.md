# Weather

Скрипт для получения текущей погоды в городе через OpenWeatherMap API.

## Установка

1. Склонируйте репозиторий:
```bash
git clone git@github.com:tamoykinden/weather_api.git
cd weather_test
```

2. Создайте виртуальное окружение:
```bash
python -m venv .venv
source venv/bin/activate
```

3. Установите зависимости
```bash
pip install -r requirements.txt
```

4. Создайте файл .env на основе .env.example и добавьте ваш API-ключ:
```text
WEATHER_API_KEY=ваш_ключ
```

5. Запуск
```bash
python3 weather.py <город>
```

Пример:

```bash
python3 weather.py Москва
python3 weather.py НьюЙорк
python3 weather.py Владимир
```

Пример вывода:
```text
Город: Москва, RU
Температура: 17.24°C
Описание: пасмурно
```