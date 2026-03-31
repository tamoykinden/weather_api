class WeatherData:
    """Хранит данные о погоде."""

    def __init__(self, city: str, country: str, temperature: float, description: str):
        """Инициализация данных о погоде."""

        self.city = city
        self.country = country
        self.temperature = temperature
        self.description = description
