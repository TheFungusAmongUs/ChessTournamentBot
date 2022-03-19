import json
import toml
from typing import Any, MutableMapping, TextIO, TYPE_CHECKING

if TYPE_CHECKING:
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


def write_json(fp: TextIO, to_write: dict) -> None:
    fp.seek(0)
    fp.truncate()
    json.dump(to_write, fp)
    fp.seek(0)


def write_toml(fp: TextIO, to_write: toml_dict) -> None:
    fp.seek(0)
    fp.truncate()
    toml.dump(to_write, fp)
    fp.seek(0)
