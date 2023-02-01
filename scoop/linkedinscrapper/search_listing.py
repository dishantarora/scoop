"""
    TODO: Write module docstring
"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from scoop.linkedinscrapper.resources.locator import Locator


class SearchListing():
    """
        TODO: Write class docstring
    """

    def __init__(self, driver):
        self._driver = driver

    def enter_job_title(self, value: str) -> None:
        """
            TODO: Write method docstring
        """
        try:
            element = self._driver.find_element(By.XPATH, Locator.job_search_title)
            element.clear()
            element.send_keys(value)
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def enter_job_location(self, value: str) -> None:
        """
            TODO: Write method docstring
        """
        try:
            element = self._driver.find_element(By.XPATH, Locator.job_search_location)
            element.clear()
            element.send_keys(value)
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def click_search_jobs_button(self):
        """
            TODO: Write method docstring
        """
        try:
            self._driver.find_element(
                By.XPATH, Locator.search_jobs_button).click()
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_job_cards(self):
        """
            TODO: Write method docstring
        """
        try:
            return self._driver.find_elements(By.CLASS_NAME, Locator.job_cards)
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_job_title(self):
        """
            TODO: Write method docstring
        """
        try:
            return self._driver.find_element(By.CLASS_NAME, Locator.job_title).text
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_job_location(self):
        """
            TODO: Write method docstring
        """
        try:
            return self._driver.find_element(By.CLASS_NAME, Locator.job_location).text
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_company_name(self):
        """
            TODO: Write method docstring
        """
        try:
            return self._driver.find_element(By.CLASS_NAME, Locator.company_name).text
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_job_posting_date(self):
        """
            TODO: Write method docstring
        """
        try:
            return self._driver.find_element(By.CLASS_NAME, Locator.job_posting_date).text
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex
