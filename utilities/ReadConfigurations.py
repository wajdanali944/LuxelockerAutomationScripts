import os
from configparser import ConfigParser


def read_configuration(category,key):
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"configurations/config.ini"))
    return config.get(category,key)