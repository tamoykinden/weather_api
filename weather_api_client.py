import requests

from config import BaseConfig
from weather_data import WeatherData


class WeatherAPIClient:
    """Клиент для работы с OpenWeatherMap API."""

    def __init__(self, config: BaseConfig):
        """Инициализация клиента."""

        self.api_key = config.WEATHER_API_KEY
        self.base_url = config.BASE_URL

    def get_weather(self, city: str) -> WeatherData:
        """
        Получает погоду для указанного города.

        Возвращает обект с данными о погоде
        """

        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ru',
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        return WeatherData(
            city=data['name'],
            country=data['sys']['country'],
            temperature=data['main']['temp'],
            description=data['weather'][0]['description'],
        )
