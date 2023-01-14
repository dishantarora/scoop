"""
    TODO: Write module docstring
"""
import toml
from src.core.base_config import BaseConfig

class Config(BaseConfig):
    """
        TODO: Write class docstring.
    """

    # This is a class variable associated with class itself
    # to keep track of whether the class has been created or not.
    __instance = None

    # This is used to eleminate the side effect of class initialization in python.
    #
    __inited = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__()
        return cls.__instance

    def __init__(self) -> None:
        if self.__inited:
            return
        self.__inited = True
        try:
            super().__init__()
            self.__config = toml.load("config-local.toml")
        except Exception as ex:
            raise ex

    def get_value(self, section: str, key: str) -> str:
        """
            TODO: Write method docstring
        """
        return self.__config[section][key]

    def get_application_value(self, key: str) -> str:
        """
            TODO: Write method docstring
        """
        return self.__config["Application"][key]
