from pydantic_settings import BaseSettings, SettingsConfigDict


class DotEnvSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    HOST: str = "0.0.0.0"
    PORT: int = 8088
    SECRET_KEY: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str


dot_env_settings = DotEnvSettings()
