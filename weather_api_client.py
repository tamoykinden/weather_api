import requests
from requests.exceptions import ConnectionError as RequestsConnectionError
from requests.exceptions import Timeout

from config import BaseConfig
from exceptions import WeatherAPIError
from weather_data import WeatherData


class WeatherAPIClient:
    """Клиент для работы с OpenWeatherMap API."""

    def __init__(self, config: BaseConfig):
        """Инициализация клиента."""

        self.api_key = config.WEATHER_API_KEY
        self.base_url = config.BASE_URL
        self.timeout = 10

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

        try:
            response = requests.get(self.base_url, params=params)
        except Timeout as e:
            raise WeatherAPIError.network_error(f'Таймаут {self.timeout} сек')
        except RequestsConnectionError:
            raise WeatherAPIError.network_error('Нет соединения с интернетом')

        if response.status_code == 404:
            raise WeatherAPIError.city_not_found(city)
        elif response.status_code == 401:
            raise WeatherAPIError.invalid_api_key()
        elif response.status_code != 200:
            raise WeatherAPIError.api_response_error(f'статус {response.status_code}')

        try:
            data = response.json()
        except Exception:
            raise WeatherAPIError.api_response_error('Невалидный JSON в ответе API')

        try:
            return WeatherData(
                city=data['name'],
                country=data['sys']['country'],
                temperature=data['main']['temp'],
                description=data['weather'][0]['description'],
            )
        except KeyError:
            raise WeatherAPIError.api_response_error('Неожиданная структура ответа API')
