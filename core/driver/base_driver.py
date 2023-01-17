from abc import ABC


class BaseDriver(ABC):

    def __init__(self):
        self._driver = None

    def load_application(self, url: str) -> None:
        self._driver.get(url)

    def close_driver(self):
        if self._driver is not None:
            self._driver.quit()
            self._driver = None

    def get_driver(self):
        return self._driver
