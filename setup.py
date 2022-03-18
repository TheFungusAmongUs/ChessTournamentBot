from setuptools import setup
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

    setup(
        name='gtahs_bot',
        version='0.1',
        description='Discord Bot for the GTA High School Chess Tournament',
        url='https://github.com/TheFungusAmongUs/gtahs_bot',
        author='TheFungusAmongUs',
        author_email='nathan.pfeffer@protonmail.com',
        license='MIT',
        packages=['gtahs_bot'],
        include_package_data=True,
        install_requires=[
            'git+https://github.com/Rapptz/discord.py',
            'toml',
            'openpyxl'
        ],
        zip_safe=False
    )

    load_files("config")
    load_files("data")


if __name__ == "__main__":
    full_setup()
