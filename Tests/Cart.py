import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Cart(unittest.TestCase):
    CART_BTN = (By.XPATH, '//div[@class="shopping_cart"]//parent::a[@title="View my shopping cart"]')
    EMPTY_CART_ERR = (By.XPATH, '//*[contains(text(),"shopping cart is empty")]')
    BLOUSE = (By.XPATH, '(//div[@class="button-container"]//parent::a[@data-id-product="2"])[1]')
    PROCEED_CHECKOUT = (By.XPATH, '(//div[@class="button-container"]//parent::a)[1]')
    DELETE_ITEM = (By.XPATH, '//td[@class="cart_delete text-center"]')
    PLUS_BTN = (By.XPATH, '//a[@data-field-qty="qty"]//i[@class="icon-plus"]')
    BLOUSE_MORE_BTN = (By.XPATH, '(//div[@class="button-container"]//parent::a[@title="View"])[2]')
    BLOUSE_TITLE = (By.XPATH, '//div[@class="pb-center-column col-xs-12 col-sm-4"]//parent::h1')
    ADD_TO_CART = (By.XPATH, '//button[@class="exclusive"]')
    TOTAL = (By.XPATH, '//span[@id="total_price"]')
    SIZE_MENU = (By.XPATH, '//select[@id="group_1"]')
    CART_QUANTITY = (By.XPATH, '//a[@id="cart_quantity_up_2_10_0_708877"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.get('http://automationpractice.com/index.php')
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        self.chrome.quit()

    def test_empty_cart_error(self):
        self.chrome.find_element(*self.CART_BTN).click()
        err_msg = self.chrome.find_element(*self.EMPTY_CART_ERR).text
        self.assertIn(err_msg, 'Your shopping cart is empty.', 'Not the correct empty cart msg error')

    def test_delete_cart_functionality(self):
        a = ActionChains(self.chrome)
        m = self.chrome.find_element(By.LINK_TEXT, "Blouse")
        a.move_to_element(m).perform()
        self.chrome.find_element(*self.BLOUSE).click()
        self.chrome.find_element(*self.PROCEED_CHECKOUT).click()
        self.chrome.find_element(*self.DELETE_ITEM).click()
        msg = self.chrome.find_element(*self.EMPTY_CART_ERR).text
        self.assertIn(msg, 'Your shopping cart is empty.', 'Not the correct empty cart msg error')

    def test_quantity_increase_btn(self):
        a = ActionChains(self.chrome)
        m = self.chrome.find_element(By.LINK_TEXT, "Blouse")
        a.move_to_element(m).perform()
        self.chrome.find_element(*self.BLOUSE).click()
        self.chrome.find_element(*self.PROCEED_CHECKOUT).click()
        self.chrome.find_element(*self.CART_QUANTITY).click()
        time.sleep(1)
        nr = self.chrome.find_element(*self.TOTAL).text
        self.assertIn(nr, '$56.00', 'Not the correct price')

    def test_cart_more_btn(self):
        a = ActionChains(self.chrome)
        m = self.chrome.find_element(By.LINK_TEXT, "Blouse")
        a.move_to_element(m).perform()
        self.chrome.find_element(*self.BLOUSE_MORE_BTN).click()
        expected = self.chrome.find_element(*self.BLOUSE_TITLE).text
        actual = 'Blouse'
        self.assertEqual(expected, actual, 'Incorrect title match')

    def test_more_quantity_btn(self):
        a = ActionChains(self.chrome)
        m = self.chrome.find_element(By.LINK_TEXT, "Blouse")
        a.move_to_element(m).perform()
        self.chrome.find_element(*self.BLOUSE_MORE_BTN).click()
        self.chrome.find_element(*self.PLUS_BTN).click()
        time.sleep(1)
        self.chrome.find_element(*self.ADD_TO_CART).click()
        self.chrome.find_element(*self.PROCEED_CHECKOUT).click()
        expected = self.chrome.find_element(*self.TOTAL).text
        actual = '$56.00'
        self.assertEqual(expected, actual, 'Incorrect price match')

    def test_check_correct_data_selected_cart(self):
        a = ActionChains(self.chrome)
        m = self.chrome.find_element(By.LINK_TEXT, "Blouse")
        a.move_to_element(m).perform()
        self.chrome.find_element(*self.BLOUSE_MORE_BTN).click()
        self.chrome.find_element(*self.PLUS_BTN).click()
        self.chrome.find_element(By.XPATH, '//option[@value="2"]').click()
        self.chrome.find_element(By.XPATH, '//a[@id="color_8"]').click()
        self.chrome.find_element(*self.ADD_TO_CART).click()
        self.chrome.find_element(*self.PROCEED_CHECKOUT).click()
        time.sleep(1)
        expected = self.chrome.find_element(By.XPATH, '(//td[@class="cart_description"]//parent::small)[2]//parent::a').text
        actual = 'Color : White, Size : M'
        self.assertEqual(expected, actual, 'Incorrect item data match')

