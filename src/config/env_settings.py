import os
from typing import Optional

from dotenv import find_dotenv, load_dotenv
   

class AppSettings:
    def __init__(self) -> None:
        self.secret_key = os.environ.get('APP_SECRET_KEY')
        self.debug = os.environ.get('APP_DEBUG', 'True').lower() == 'true'
        
        self.__validate_settings()
    
    def __validate_settings(self) -> None:
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
        
        self.__validate_settings()
        
    def __validate_settings(self) -> None:
        required_fields = {
            'DB_NAME': self.__name,
            'DB_USER': self.__user,
            'DB_PASSWORD': self.__password,
            'DB_HOST': self.__host,
            'DB_PORT': self.__port
        }
        missing_fields = [field for field, value in required_fields.items() if not value]
        
        if missing_fields:
            raise ValueError(f"Missing required database settings: {', '.join(missing_fields)}")
    
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


def load_env_settings(file_name: Optional[str] = '.env') -> None:
    env_file = find_dotenv(file_name)
    
    if not env_file:
        raise FileNotFoundError(f'Environment file "{file_name}" not found.')
    
    load_dotenv(env_file)
    

def get_app_settings() -> AppSettings:
    return AppSettings()


def get_db_settings() -> DBSettings:
    return DBSettings()
