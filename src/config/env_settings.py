import os
from typing import Optional

from dotenv import find_dotenv, load_dotenv

    
class EnvSettings:
    def __init__(self, file_name: Optional[str]) -> None:
        self.__env_file = find_dotenv(file_name)
        
        if not self.__env_file:
            raise FileNotFoundError(f'Environment file "{file_name}" not found.')
        
        load_dotenv(self.__env_file)
        

class AppSettings:
    def __init__(self) -> None:
        self.secret_key = os.environ.get('APP_SECRET_KEY')
        self.debug = os.environ.get('APP_DEBUG', 'True').lower() == 'true'
        
        if not self.secret_key:
            raise ValueError(f'APP_SECRET_KEY is not set in the environment variables.')
        

class DBSettings:
    def __init__(self):
        self.__engine = 'django.db.backends.postgresql'
        self.__name = os.environ.get('DB_NAME')
        self.__user = os.environ.get('DB_USER')
        self.__password = os.environ.get('DB_PASSWORD')
        self.__host = os.environ.get('DB_HOST')
        self.__port = os.environ.get('DB_PORT')
    
    @property
    def get_config(self) -> dict:
        return {
            'ENGINE': self.__engine,
            'NAME': self.__name,
            'USER': self.__user,
            'PASSWORD': self.__password,
            'HOST': self.__host,
            'PORT': self.__port,
        }
        

def get_env_settings(file_name: Optional[str] = '.env') -> EnvSettings:
    return EnvSettings(file_name)


def get_app_settings() -> AppSettings:
    return AppSettings()


def get_db_settings() -> DBSettings:
    return DBSettings()
