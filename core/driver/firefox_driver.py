from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from core.driver.base_driver import BaseDriver


class FireFoxDriver(BaseDriver):

    def __init__(self, config) -> None:
        super().__init__()
        self.__config = config
        self.__setup()

    def __setup(self):
        options = Options()
        options.binary_location = self.__config.get_browser_value(
            'firefox_binary_location')
        self._driver = webdriver.Firefox(executable_path=self.__config.get_browser_value(
            'firefox_driver_path'), options=options)