import os
from abc import ABC
import yaml

class Setting(ABC):
    def __init__(self):
        self._some = self.__load()

    def __load(self,):
        with open(os.path.abspath('settings.yml'), 'r', encoding='utf-8') as file:
            temp = yaml.safe_load(file)
        return temp['system_setting']
