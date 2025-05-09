from pydantic import BaseSettings

class Settings(BaseSettings):
    azure_api_type: str
    azure_api_version: str
    azure_api_base: str
    azure_api_key: str
    azure_engine: str

    class Config:
        env_file = ".env"

settings = Settings()
