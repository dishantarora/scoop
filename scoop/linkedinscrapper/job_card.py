"""
    TODO: Write module docstring
"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from scoop.linkedinscrapper.locator import Locator


class JobCard():
    """
        TODO: Write class docstring
    """

    def __init__(self, web_element):
        self._web_element = web_element

    def get_job_title(self):
        """
            TODO: Write method docstring
        """
        try:
            return self._web_element.find_element(By.CLASS_NAME, Locator.job_title).text
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_job_location(self):
        """
            TODO: Write method docstring
        """
        try:
            return self._web_element.find_element(By.CLASS_NAME, Locator.job_location).text
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_company_name(self):
        """
            TODO: Write method docstring
        """
        try:
            return self._web_element.find_element(By.CLASS_NAME, Locator.company_name).text
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_job_posting_date(self):
        """
            TODO: Write method docstring
        """
        try:
            return self._web_element.find_element(By.CLASS_NAME, Locator.job_posting_date).get_attribute('datetime')
        except NoSuchElementException as ex:
            raise ex
        except Exception as ex:
            raise ex
