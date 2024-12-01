from selenium import webdriver
from selenium.webdriver.common.by import By


class Product:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.NAME, "add-to-cart").click()

    def summary(self):
        return self.driver.find_element(By.CLASS_NAME, "summary")

    def name(self):
        return self.summary().find_element(By.CLASS_NAME, "product_title").text

    def price(self):
        return self.summary().find_elements(By.TAG_NAME, "bdi")[-1].text[:-2]  # slicing the sign


