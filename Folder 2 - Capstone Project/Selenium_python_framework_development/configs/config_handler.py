import configparser
import os

class ConfigHandler:
    _parser = configparser.ConfigParser()
    _path = os.path.join(os.path.dirname(__file__), 'system.ini')
    _parser.read(_path)

    @classmethod
    def get_url(cls):
        return cls._parser.get('Settings', 'target_url')

    @classmethod
    def get_wait_time(cls):
        return int(cls._parser.get('Settings', 'explicit_wait'))