from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from core.util.system_setting import SystemSetting
from core.driver.driver_factory import DriverFactory
from scoop.amazonscrapper.app_setting import AppSetting
from scoop.amazonscrapper.locators import Locator


def main():

    # Initializing and setting up system settings used mainly in dependency injection
    system_setting = SystemSetting()
    
    # Initializing and setting up application settings used mainly in dependency injection
    app_setting = AppSetting()

    # Setting and initializing web driver object.
    driver = DriverFactory().get_instance(system_setting)
    driver.get(app_setting.application_url)

    # Enter search keyword in search field and submit.
    try:
        search_field = driver.find_element(By.XPATH, Locator.SEARCH_FIELD)
    except NoSuchElementException:
        exit()

    try:
        search_button = driver.find_element(By.XPATH, Locator.SEARCH_BUTTON)
    except NoSuchElementException:
        exit()

    search_field.clear()
    search_field.send_keys(app_setting.search_product)
    search_button.click()

    # Verifying search result page.

    search_result_items = driver.find_elements(
        By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']")

    products = []

    for item in search_result_items:
        temp = {}
        product_heading = item.find_element(
            By.XPATH,
            "//div/h2/a/span[@class='a-size-medium a-color-base a-text-normal']")
        if product_heading is not None:
            temp['product_heading'] = product_heading.text
        else:
            temp['product_heading'] = 'Not Found'
        # temp['rating'] = item.find_element(By.XPATH, '').text
        # temp['customer_reviews'] = item.find_element(By.XPATH, '').text
        # temp['current_price'] = item.find_element(By.XPATH, '').text
        # temp['actual_price'] = item.find_element(By.XPATH, '').text
        # temp['amount_saved'] = item.find_element(By.XPATH, '').text
        # temp['amount_saved_percentage'] = item.find_element(By.XPATH, '').text
        # temp['is_no_cost_emi_available'] = item.find_element(By.XPATH, '').text
        # temp['free_delivery_by'] = item.find_element(By.XPATH, '').text
        # temp['is_prime'] = item.find_element(By.XPATH, '').text
        products.append(temp)

    print(len(products))

    for product in products:
        print(product['product_heading'])

    driver.quit()


if __name__ == '__main__':
    main()
