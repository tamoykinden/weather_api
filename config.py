import os

from dotenv import load_dotenv


class BaseConfig:
    """Конфигурация проекта."""

    def __init__(self):
        load_dotenv()
        self.WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
