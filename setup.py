import toml
from pathlib import Path


def load_files(to_load: str):
    # Will be used to load both the data and the config files.
    if Path(f'{to_load}/{to_load}.toml').exists():
        with open(f"{to_load}/{to_load}.toml", "r+") as file, open(f"{to_load}/base_{to_load}.toml", "r") as base_file:
            # Adds any extra fields from the base config file when updating the bot
            base_toml = toml.load(base_file)
            current_toml = toml.load(file)
            toml.dump({**base_toml, **current_toml}, file)

    else:
        with open(f"{to_load}/{to_load}.toml", "w") as file, open(f"{to_load}/base_{to_load}.toml", "r") as base_file:
            toml.dump(toml.load(base_file), file)


def full_setup():

    load_files("config")
    load_files("data")


if __name__ == "__main__":
    full_setup()
