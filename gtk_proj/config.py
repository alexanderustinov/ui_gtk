import tomllib

from pathlib import Path

from platformdirs import user_config_dir

from . import __name__

config_dir = Path(user_config_dir())/__name__
config_file = (config_dir/'config.toml')
if not config_dir.exists():
    config_dir.mkdir()
    config_file.touch()

default_config_file = Path(__file__).parent/'default_config.toml'

with open(default_config_file, 'rb') as f:
    config = tomllib.load(f)

with open(config_file, 'rb') as f:
    config.update(tomllib.load(f))

print(config)
