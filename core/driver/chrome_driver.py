from selenium import webdriver
from core.driver.base_driver import BaseDriver


class ChromeDriver(BaseDriver):

    def __init__(self, config) -> None:
        super().__init__()
        self.__config = config
        self.__setup()

    def __setup(self):
        self._driver = webdriver.Chrome(
            self.__config.get_browser_value('chrome_driver_path'))
