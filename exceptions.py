class WeatherAPIError(Exception):
    """Базовое исключение для всех ошибок API."""

    def __init__(self, message: str, status_code: int = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    @classmethod
    def city_not_found(cls, city: str = None):
        """Создаёт ошибку 'Город не найден'."""

        msg = f'Город не найден: {city}' if city else 'Город не найден'
        return cls(msg, status_code=404)

    @classmethod
    def invalid_api_key(cls):
        """Создаёт ошибку 'Неверный API ключ'."""

        return cls('Неверный API ключ. Проверьте .env файл', status_code=401)

    @classmethod
    def network_error(cls, details: str = None):
        """Создаёт ошибку сети."""

        msg = f'Ошибка сети: {details}' if details else 'Ошибка сети'
        return cls(msg)

    @classmethod
    def api_response_error(cls, details: str = None):
        """Создаёт ошибку неожиданного ответа API."""

        msg = f'Неожиданный ответ API: {details}' if details else 'Неожиданный ответ API'
        return cls(msg)
