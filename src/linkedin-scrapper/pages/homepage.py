"""
    TODO: Write module docstring
"""
from resources.locator import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Homepage():
    """
        TODO: Write class docstring
    """

    def __init__(self, locator):
        self.locator = locator
        self.driver = webdriver.Chrome()
        self.__init_locators()

    def __init_locators(self):
        try:
            self.job_title = self.driver.find_element(By.XPATH, Locator.job_title_search_field)
            self.location = self.driver.find_element(By.XPATH, Locator.location_search_field)
            self.search_jobs = self.driver.find_element(By.XPATH, Locator.search_jobs_button)
            self.sign_in = self.driver.find_element(By.XPATH, Locator.sign_in_button)
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def enter_job_title(self, value):
        """
            TODO: Write method docstring
        """ 
        try:
            self.job_title.send_keys(value)
        except Exception as ex:
            raise ex

    def enter_location(self, value):
        """
            TODO: Write method docstring
        """
        try:
            self.location.send_keys(value)
        except Exception as ex:
            raise ex

    def click_search_jobs_button(self):
        """
            TODO: Write method docstring
        """
        try:
            self.search_jobs.click()
        except Exception as ex:
            raise ex

    def click_sign_in_button(self):
        """
            TODO: Write method docstring
        """
        try:
            self.sign_in.click()
        except Exception as ex:
            raise ex
