from selenium import webdriver
from core.driver.base_driver import BaseDriver


class ChromeDriver(BaseDriver):

    def __init__(self, system_setting) -> None:
        super().__init__()
        self.__system_setting = system_setting
        self.__setup()

    def __setup(self):
        self._driver = webdriver.Chrome(executable_path=self.__system_setting.chrome_driver_path)
