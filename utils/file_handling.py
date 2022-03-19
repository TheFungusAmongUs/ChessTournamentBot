import json
import toml
from typing import Any, MutableMapping, TextIO, TYPE_CHECKING

toml_dict = MutableMapping[str, Any]


def read_json(fp: TextIO) -> dict:
    fp.seek(0)
    data: dict = json.load(fp)
    fp.seek(0)
    return data


def read_toml(fp: TextIO) -> toml_dict:
    fp.seek(0)
    data: toml_dict = toml.load(fp)
    fp.seek(0)
    return data


def write_json(to_write: dict, fp: TextIO) -> None:
    fp.seek(0)
    fp.truncate()
    json.dump(to_write, fp)
    fp.seek(0)


def write_toml(to_write: toml_dict, fp: TextIO) -> None:
    fp.seek(0)
    fp.truncate()
    toml.dump(to_write, fp)
    fp.seek(0)


# Attribution: Archit Dwidedi, Stack Overflow: https://stackoverflow.com/a/49003922/16177247
def get_json(obj):
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
    )
