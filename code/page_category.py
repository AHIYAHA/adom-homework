from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Category:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def sorting(self):
        return Select(self.driver.find_element(By.NAME, "orderby"))

    def order_by(self, option):
        """options: menu_order, popularity, rating, date, price, price-desc"""
        self.sorting().select_by_value(option)

    def list_of_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "product")

    def price_of_product_in_index(self, i):
        return self.list_of_products()[i].find_elements(By.TAG_NAME, "bdi")[-1].text[:-2]  # slicing the sign

    def list_of_prices(self):
        return [float(self.price_of_product_in_index(i)) for i in range(len(self.list_of_products()))]
