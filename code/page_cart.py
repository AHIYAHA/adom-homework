from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def products(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")

    def name_of_product(self, i):
        return self.products()[i].find_element(By.CLASS_NAME, "product-name").text

    def price_of_product(self, i):
        return self.products()[i].find_element(By.CLASS_NAME, "product-price").text[:-2]  # slicing the sign

    def select_shipping_method(self, i, text):
        """
        0 - Local pickup, 0₪
        1 - Delivery Express, 12.50 ₪
        2 - Registered Mail, 5.90 ₪
        waiting until the total price is changing to the given text
        """
        self.driver.find_elements(By.CSS_SELECTOR, "[type='radio']")[i].click()
        try:
            self.wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "strong"), text))
        except:
            print("error - the order price is not updated when selection a shipping method")

    def total(self):
        return self.driver.find_element(By.TAG_NAME, "strong").text[:-2]  # slicing the sign

    def checkout_button(self):
        return self.driver.find_element(By.CLASS_NAME, "wc-proceed-to-checkout")
