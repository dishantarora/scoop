"""
    TODO: Write module docstring
"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from scoop.linkedinscrapper.resources.locator import Locator


class Homepage():
    """
        TODO: Write class docstring
    """

    def __init__(self, driver):
        self.__driver = driver

    def click_jobs_button(self):
        """
            TODO: Write method docstring
        """
        try:
            self.__driver.find_element(By.XPATH, Locator.jobs_button).click()
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex
