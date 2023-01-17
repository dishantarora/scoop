import os
import toml


class Config():

    def __init__(self):
        self.__config = toml.load(os.path.abspath("settings.toml"))

    def get_config_value(self, section: str, key: str) -> str:
        return self.__config[section][key]

    def get_webdriver_value(self, key: str) -> str:
        return self.__config['WebDriver'][key]

    def get_browser_value(self, key: str) -> str:
        return self.__config['Browser'][key]

    def get_browser_resolution_value(self, key: str) -> str:
        return self.__config['Browser']['Resolution'][key]
