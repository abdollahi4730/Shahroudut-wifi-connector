from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    username : str
    password : str
    headless : bool
    
    model_config = SettingsConfigDict(case_sensitive=False, env_file='.env')

settings = Settings()
