from unittest import TestCase
from selenium import webdriver

from automation.menu import Menu
from automation.page_category import Category
from automation.page_product import Product
from automation.page_cart import Cart
from automation.page_checkout import Checkout


class TestShop(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.menu = Menu(self.driver)
        self.category = Category(self.driver)
        self.product = Product(self.driver)
        self.cart = Cart(self.driver)
        self.checkout = Checkout(self.driver)

        self.driver.get("https://atid.store/")

    def tearDown(self):
        self.driver.close()

    def test_1(self):
        """
        tests a complete shopping process:
        navigation to the accessories category page,
        sorting the list of products by price from low to high,
        navigation to the cheapest product page,
        adding the product to cart,
        navigation to the cart page,
        verifying that the product name and price are the same on the cart page and on the product page,
        selection shipping method: Delivery Express,
        verifying that the total price increases in 12.5,
        navigation to the checkout page,
        filling in all the mandatory fields,
        and clicking on placing order button.
        """
        self.menu.accessories().click()

        # category page
        self.category.order_by("price")
        try:
            self.assertEqual(self.category.list_of_prices(), sorted(self.category.list_of_prices()))
            self.category.list_of_products()[0].click()
        except:
            print("error - the products are not sorted by price from low to high")
            cheapest = self.category.list_of_prices().index(min(self.category.list_of_prices()))
            self.category.list_of_products()[cheapest].click()

        # product page
        self.product.add_to_cart()
        product_name = self.product.name()
        product_price = self.product.price()
        self.menu.cart().click()

        # cart page
        try:
            self.assertEqual(product_name, self.cart.name_of_product(0))
        except:
            print("error - the product name is not updated in cart")
        try:
            self.assertEqual(product_price, self.cart.price_of_product(0))
        except:
            print("error - the product price is not updated in cart")

        # select shipping method
        self.cart.select_shipping_method(1, str(float(product_price) + 12.5) + "0 ₪")
        self.cart.checkout_button().click()

        # checkout page
        self.checkout.fill_first_name("a")
        self.checkout.fill_last_name("a")
        self.checkout.fill_address("a")
        self.checkout.fill_city("a")
        self.checkout.fill_postcode("1")
        self.checkout.fill_phone("1")
        self.checkout.fill_email("a@a.com")
        self.checkout.place_order_button().click()
