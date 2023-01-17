#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.util.config import Config
from core.util.app_settings import AppSetting
from core.driver.driver_factory import DriverFactory
from scoop.linkedinscrapper.pages.job_card import JobCard
from scoop.linkedinscrapper.pages.homepage import Homepage
from scoop.linkedinscrapper.pages.search_listing import SearchListing


def main():

    # Reading configuration file.
    # config = Config()
    app_setting = AppSetting()

    # Setting up webdriver and loading application.
    driver = DriverFactory().get_instance(app_setting.target_browser)
    driver.get(app_setting.application_url)

    # Open Homepage and click on jobs links at the top of webpage.
    homepage = Homepage(driver)
    homepage.click_jobs_button()

    # Creating a storage for jobs data.
    jobs = []

    # Searching jobs.
    search_listing_page = SearchListing(driver)
    search_listing_page.enter_job_title("Software Engineer")
    search_listing_page.enter_job_location("Delhi, India")
    search_listing_page.click_search_jobs_button()

    # Extracting data from each job card.
    job_cards = search_listing_page.get_job_cards()
    for each_card in job_cards:
        job = {}
        job_card = JobCard(each_card)
        job['title'] = job_card.get_job_title()
        job['company_name'] = job_card.get_company_name()
        job['location'] = job_card.get_job_location()
        job['posting_date'] = job_card.get_job_posting_date()
        jobs.append(job)
    print(jobs)

    # Quitting application.
    driver.quit()


if __name__ == "__main__":
    main()
