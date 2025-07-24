from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    BOT_TOKEN: str
    OPENAI_API_KEY: str
    QDRANT_API_KEY: str
    model_config = SettingsConfigDict(env_file=".env")
settings = Settings()  # type: ignore
