from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""

    app_name: str = "ViraSearch API"
    debug: bool = True
    api_version: str = "v1"

    # Database settings (add when needed)
    # database_url: Optional[str] = None

    # CORS settings
    cors_origins: list = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
