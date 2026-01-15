from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Budget App Backend"
    DATABASE_URL: str = "postgresql://budget:budget58@db:5432/budgetdb"
    SECRET_KEY: str = "bakaibankisonelove"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        env_file = ".env"
        
settings = Settings()