from pathlib import Path
from utils.file_handling import *


def setup_toml() -> None:
    if Path('config/config.toml').exists():
        with open("config/config.toml", "r+") as file, open("config/base_config.toml", "r") as base_file:
            # Adds any extra fields from the base config file when updating the bot
            base_toml = read_toml(base_file)
            current_toml = read_toml(file)
            write_toml({**base_toml, **current_toml}, file)

    else:
        with open("config/config.toml", "w") as file, open("config/base_config.toml", "r") as base_file:
            write_toml(toml.load(base_file), file)


if __name__ == "__main__":
    setup_toml()
