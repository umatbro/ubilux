"""
Add environment variables to the App Engine config file
"""

import argparse
import os
import pathlib
import sys

import dotenv

import yaml

parser = argparse.ArgumentParser(
    description="Add required environment variables to the App Engine config files"
)
parser.add_argument(
    "file_path", nargs="?", default="app.yml", help="Path to the config file"
)


UPDATE_ENV_VARS = {
    "REDIS_HOST",
    "REDIS_PORT",
    "REDIS_DB",
    "REDIS_PASSWORD",
    "DEBUG",
}


if __name__ == "__main__":
    args = parser.parse_args()
    env_file_path = (pathlib.Path(".") / ".env").absolute()
    dotenv.load_dotenv(dotenv_path=env_file_path, verbose=True)

    file_path = pathlib.Path(args.file_path).absolute()
    if not pathlib.Path(file_path).is_file():
        print(f'File "{file_path}" does not exist', file=sys.stderr)
        sys.exit(1)

    with open(file_path, "r") as stream:
        config = yaml.safe_load(stream)

    ENV_VARS_KEY = "env_variables"

    config[ENV_VARS_KEY] = config.get(ENV_VARS_KEY, None) or {}
    for key in UPDATE_ENV_VARS:
        val = os.environ.get(key, None)
        if val:
            config[ENV_VARS_KEY][key] = val

    with open(file_path, "w") as stream:
        yaml.safe_dump(config, stream)
