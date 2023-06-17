""" Питон любит чтобы все настройки запускались/ хранились вызывались из одного места
так как если в разных местах то часть настроек не подтянеться
скорее вызывались из "одного места"  """
import os

from dotenv import load_dotenv  # чтобы загружать данные из .env файла
from pydantic import BaseSettings, SecretStr, StrictStr  # базовые настройки

load_dotenv()


class SiteSettings(BaseSettings):  # это стандартный способ валидации и сокрытия чувствительных данных
    api_key: SecretStr = os.getenv('SITE_HOTTEL_API', None)  # None по умолчанию, чтобы выхватить ошибку
    api_host: StrictStr = os.getenv('HOTEL_API_HOST', None)