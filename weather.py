import argparse
import sys

from config import BaseConfig
from logger import setup_logger
from weather_api_client import WeatherAPIClient

logger = setup_logger(__name__)


def main():
    parser = argparse.ArgumentParser(description='Получить текущую погоду в городе')
    parser.add_argument('city', type=str, help='Название города')
    args = parser.parse_args()

    logger.info(f'Запрос погоды для {args.city}')

    try:
        config = BaseConfig()
    except Exception as e:
        logger.error(f'Ошибка загрузки конфигурации: {e}')
        sys.exit(1)

    if not config.WEATHER_API_KEY:
        logger.error('API ключ не найден. Проверьте файл .env')
        sys.exit(1)

    try:
        client = WeatherAPIClient(config)
        weather = client.get_weather(args.city)

        logger.info(f'Погода получена: {weather.city}, {weather.country}')
        print(f'\nГород: {weather.city}, {weather.country}')
        print(f'Температура: {weather.temperature}°C')
        print(f'Описание: {weather.description}\n')

    except Exception as e:
        logger.error(f'Ошибка при получении погоды: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
