from os import environ
from typing import Any
from dotenv import load_dotenv

from food_app.errors import EnvVarNotFound

load_dotenv()

def unpack_env_var(key: str) -> Any:
    env_var = environ.get(key)
    if env_var is None:
        raise EnvVarNotFound(f"Couldn't locate {key} in .env")
    return env_var

DATABASE_PASSWORD = unpack_env_var("DATABASE_PASSWORD")