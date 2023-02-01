from core.driver.chrome_driver import ChromeDriver
from core.driver.firefox_driver import FireFoxDriver


class DriverFactory():

    @staticmethod
    def get_instance(system_setting):
        if system_setting.target_browser.lower() == 'chrome':
            return ChromeDriver(system_setting).get_driver()
        elif system_setting.target_browser.lower() == 'firefox':
            return FireFoxDriver(system_setting).get_driver()
        else:
            return ChromeDriver(system_setting).get_driver()
