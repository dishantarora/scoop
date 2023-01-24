from selenium.webdriver.common.by import By
from core.util.system_setting import SystemSetting
from core.driver.driver_factory import DriverFactory
from scoop.amazonscrapper.app_setting import AppSetting

def main():

    # Initializing and setting up system settings used mainly in dependency injection
    system_setting = SystemSetting()
    
    # Initializing and setting up application settings used mainly in dependency injection
    app_setting = AppSetting()

    # Setting and initializing web driver object.
    driver = DriverFactory().get_instance(system_setting)
    driver.get(app_setting.application_url)

    # Enter search keyword in search field and submit.
    search_field = driver.find_element(By.XPATH, r'//*[@id="twotabsearchtextbox"]')
    search_submit_button = driver.find_element(By.XPATH, r'//*[@id="nav-search-submit-button"]')
    search_field.clear()
    search_field.send_keys(app_setting.product_name)
    search_submit_button.click()

    # Verifying search result page.

    search_result_items = driver.find_elements(By.XPATH, '')

    products = []

    for item in search_result_items:        
        temp = {}
        temp['product_heading'] = item.find_element(By.XPATH, '').text
        temp['rating'] = item.find_element(By.XPATH, '').text
        temp['customer_reviews'] = item.find_element(By.XPATH, '').text
        temp['current_price'] = item.find_element(By.XPATH, '').text
        temp['actual_price'] = item.find_element(By.XPATH, '').text
        temp['amount_saved'] = item.find_element(By.XPATH, '').text
        temp['amount_saved_percentage'] = item.find_element(By.XPATH, '').text
        temp['is_no_cost_emi_available'] = item.find_element(By.XPATH, '').text
        temp['free_delivery_by'] = item.find_element(By.XPATH, '').text
        temp['is_prime'] = item.find_element(By.XPATH, '').text
        products.append(temp)

    for product in products:
        print(product.prettify())
    
    driver.quit()

if __name__ == '__main__':
    main()
