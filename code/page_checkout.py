from selenium import webdriver
from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def first_name(self):
        return self.driver.find_element(By.ID, "billing_first_name")

    def fill_first_name(self, value):
        self.first_name().send_keys(value)

    def last_name(self):
        return self.driver.find_element(By.ID, "billing_last_name")

    def fill_last_name(self, value):
        self.last_name().send_keys(value)

    def address(self):
        return self.driver.find_element(By.ID, "billing_address_1")

    def fill_address(self, value):
        self.address().send_keys(value)

    def postcode(self):
        return self.driver.find_element(By.ID, "billing_postcode")

    def fill_postcode(self, value):
        self.postcode().send_keys(value)

    def city(self):
        return self.driver.find_element(By.ID, "billing_city")

    def fill_city(self, value):
        self.city().send_keys(value)

    def phone(self):
        return self.driver.find_element(By.ID, "billing_phone")

    def fill_phone(self, value):
        self.phone().send_keys(value)

    def email(self):
        return self.driver.find_element(By.ID, "billing_email")

    def fill_email(self, value):
        self.email().send_keys(value)

    def place_order_button(self):
        return self.driver.find_element(By.ID, "place_order")


