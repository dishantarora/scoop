import os
from abc import ABC
import yaml


class Setting(ABC):

    def __init__(self, filepath: str):
        self.__filepath = filepath
        self.__setting_data = None
        self.__read_setting_file()

    @property
    def _get_setting_data(self):
        return self.__setting_data

    def __read_setting_file(self):
        temp = None
        with open(os.path.abspath(self.__filepath), 'r', encoding='utf-8') as file:
            temp = yaml.safe_load(file)
        self.__setting_data = temp