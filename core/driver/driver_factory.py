from core.driver.chrome_driver import ChromeDriver
from core.driver.firefox_driver import FireFoxDriver
from core.util.config import Config


class DriverFactory():

    @staticmethod
    def get_instance(browser_type: str):
        config = Config()
        if browser_type.lower() == 'chrome':
            return ChromeDriver(config)
        elif browser_type.lower() == 'firefox':
            return FireFoxDriver(config)
        else:
            return ChromeDriver(config)