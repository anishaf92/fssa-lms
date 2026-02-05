from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    GOOGLE_CLIENT_ID: str

    class Config:
        env_file = ".env"

settings = Settings()
DATABASE_URL = settings.DATABASE_URL
JWT_SECRET = settings.JWT_SECRET
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
GOOGLE_CLIENT_ID = settings.GOOGLE_CLIENT_ID
