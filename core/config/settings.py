from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    location_name: str
    latitude: float
    longitude: float
    telegram_chat_id: str
    telegram_api_token: str

    class Config:
        env_file = ".env"