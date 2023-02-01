#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pandas as pd


from core.util.system_setting import SystemSetting
from core.driver.driver_factory import DriverFactory
from scoop.linkedinscrapper.job_card import JobCard
from scoop.linkedinscrapper.homepage import Homepage
from scoop.linkedinscrapper.search_listing import SearchListing
from scoop.linkedinscrapper.app_setting import AppSetting

def initializing_settings():
    return SystemSetting(), AppSetting()

def main():
    
    # Setting up both system level and application level setting instances.
    system_setting, app_setting = initializing_settings()

    # Setting up webdriver by taking target browser from system setting
    # And, loading application by receiving application url from app setting.
    driver = DriverFactory().get_instance(system_setting)
    driver.get(app_setting.application_url)

    # Open Homepage and click on jobs links at the top of webpage.
    homepage = Homepage(driver)
    homepage.click_jobs_button()

    # Searching jobs by entering job title and location mentioned in app setting file.
    search_listing_page = SearchListing(driver)
    search_listing_page.enter_job_title(app_setting.job_title)
    search_listing_page.enter_job_location(app_setting.job_location)
    search_listing_page.click_search_jobs_button()

    # Creating storage for extracted jobs.
    jobs = []

    # Extracting data from each job card.
    job_cards = search_listing_page.get_job_cards()
    for each_card in job_cards:
        job = {}
        job_card = JobCard(each_card)
        job['Title'] = job_card.get_job_title()
        job['Company Name'] = job_card.get_company_name()
        job['Location'] = job_card.get_job_location()
        job['Posting Date'] = job_card.get_job_posting_date()
        jobs.append(job)

    # Converting an array of job object into json string.
    json_string = json.dumps(jobs)
    print(json_string)

    # Converting jobs json string into excel file.
    pd.read_json(json_string).to_excel('output.xlsx')

    # Quitting application.
    driver.quit()


if __name__ == "__main__":
    main()
