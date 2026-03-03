from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:Aniket123@localhost:5432/job_assistant"

    class Config:
        env_file = ".env"

settings = Settings()