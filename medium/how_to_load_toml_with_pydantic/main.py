from dotenv_config import dot_env_settings
from json_config import json_settings
from toml_config import toml_settings
from yaml_config import yaml_settings

if __name__ == "__main__":
    print(".env result", dot_env_settings)
    print("config.toml result",toml_settings)
    print("config.json result",json_settings)
    print("config.yaml result",yaml_settings)
