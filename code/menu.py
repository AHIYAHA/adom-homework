from selenium import webdriver
from selenium.webdriver.common.by import By


class Menu:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def accessories(self):
        return self.driver.find_element(By.ID, "menu-item-671")

    def cart(self):
        return self.driver.find_element(By.ID, "ast-site-header-cart")
