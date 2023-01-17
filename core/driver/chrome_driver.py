from selenium import webdriver
from core.driver.base_driver import BaseDriver


class ChromeDriver(BaseDriver):

    def __init__(self, app_setting) -> None:
        super().__init__()
        self.__app_setting = app_setting
        self.__setup()

    def __setup(self):
        self._driver = webdriver.Chrome(self.__app_setting.chrome_driver_path)
