import os.path
from configparser import ConfigParser
from pathlib import Path


def readConfig(section,key):
    config_file_path = os.path.join(str(Path.cwd()), "Configurations", "config.ini")
    config = ConfigParser()
    config.read(config_file_path)
    return config.get(section,key)
