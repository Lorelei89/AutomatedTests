import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Account(unittest.TestCase):
    SIGN_IN = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    SIGN_IN_BTN = (By.XPATH, '//button[@id="SubmitLogin"]')
    PASS_INPUT = (By.XPATH, '//input[@id="passwd"]')
    EMAIL_ADDRESS_REGISTER = (By.XPATH, '//input[@id="email"]')

    MY_ACCOUNT = (By.XPATH, '(//div[@class="header_user_info"]//parent::a)[1]')
    ORDER_DETAILS = (By.XPATH, '(//ul[@class="myaccount-link-list"]//parent::li)[1]//parent::a')

    MY_ADDRESSES = (By.XPATH, '(//ul[@class="myaccount-link-list"]//parent::li)[3]//parent::a')
    UPDATE_ADDRESS = (By.XPATH, '(//li[@class="address_update"]//parent::a)[1]')
    FIRST_NAME = (By.XPATH, '//input[@id="firstname"]')
    LAST_NAME = (By.XPATH, '//input[@id="lastname"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@id="address1"]')
    CITY_FIELD = (By.XPATH, '//input[@id="city"]')
    STATE_FIELD = (By.XPATH, '//select[@name="id_state"]')
    ZIP_FIELD = (By.XPATH, '//input[@id="postcode"]')
    MOBILE_PHONE = (By.XPATH, 'input[@id="phone_mobile"]')
    HOME_PHONE = (By.XPATH, 'input[@id="phone"]')
    SAVE_BTN = (By.XPATH, '//button[@id="submitAddress"]')
    IS_REQUIRED_ERR = (By.XPATH, '//li[contains(text(),"is required")]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.get('http://automationpractice.com/index.php')
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.SIGN_IN).click()
        self.chrome.find_element(*self.MY_ACCOUNT).click()

    def tearDown(self):
        self.chrome.quit()

    def login(self):
        self.chrome.find_element(*self.EMAIL_ADDRESS_REGISTER).send_keys('darkstar_mary@yahoo.com')
        self.chrome.find_element(*self.PASS_INPUT).send_keys('Pass234@#$')
        self.chrome.find_element(*self.SIGN_IN_BTN).click()

    def login_my_addresses_section(self):
        self.login()
        self.chrome.find_element(*self.MY_ADDRESSES).click()
        self.chrome.find_element(*self.UPDATE_ADDRESS).click()

    def test_no_orders_msg(self):
        self.login()
        self.chrome.find_element(*self.ORDER_DETAILS).click()
        msg = self.chrome.find_element(By.XPATH, '//p[contains(text(), "not placed")]').text
        self.assertIn(msg, 'You have not placed any orders.', 'Not the correct message')

    def test_update_firstname_input_msg(self):
        self.login_my_addresses_section()
        self.chrome.find_element(*self.FIRST_NAME).clear()
        self.chrome.find_element(*self.FIRST_NAME).send_keys('FirstName')
        self.chrome.find_element(*self.SAVE_BTN).click()
        expected = self.chrome.find_element(By.XPATH, '(//span[@class="address_name"])[1]').text
        actual = 'FirstName'
        self.assertEqual(expected, actual, 'Data is not correct')

    def test_my_addresses_delete__firstname_err(self):
        self.login_my_addresses_section()
        self.chrome.find_element(*self.FIRST_NAME).clear()
        self.chrome.find_element(*self.SAVE_BTN).click()
        err_msg = self.chrome.find_element(*self.IS_REQUIRED_ERR).text
        self.assertIn(err_msg, 'firstname is required.', 'Not the correct input error')

    def test_my_addresses_delete_lastname_err(self):
        self.login_my_addresses_section()
        self.chrome.find_element(*self.LAST_NAME).clear()
        self.chrome.find_element(*self.SAVE_BTN).click()
        err_msg = self.chrome.find_element(*self.IS_REQUIRED_ERR).text
        self.assertIn(err_msg, 'lastname is required.', 'Not the correct input error')

    def test_delete_address_field_err(self):
        self.login_my_addresses_section()
        self.chrome.find_element(*self.ADDRESS_FIELD).clear()
        self.chrome.find_element(*self.SAVE_BTN).click()
        err_msg = self.chrome.find_element(*self.IS_REQUIRED_ERR).text
        self.assertIn(err_msg, 'address1 is required.', 'Not the correct input error')

    def test_delete_city_field_err(self):
        self.login_my_addresses_section()
        self.chrome.find_element(*self.CITY_FIELD).clear()
        self.chrome.find_element(*self.SAVE_BTN).click()
        err_msg = self.chrome.find_element(*self.IS_REQUIRED_ERR).text
        self.assertIn(err_msg, 'city is required.', 'Not the correct input error')

    def test_delete_state_field_err(self):
        self.login_my_addresses_section()
        self.chrome.find_element(*self.STATE_FIELD).click()
        self.chrome.find_element(By.XPATH, '(// select[@ name="id_state"] // parent::option)[1]').click()
        self.chrome.find_element(*self.SAVE_BTN).click()
        err_msg = self.chrome.find_element(By.XPATH, '//li[contains(text(),"requires")]').text
        self.assertIn(err_msg, 'This country requires you to chose a State.', 'Not the correct input error')

    def test_delete_zip_code_err(self):
        self.login_my_addresses_section()
        self.chrome.find_element(*self.ZIP_FIELD).clear()
        self.chrome.find_element(*self.SAVE_BTN).click()
        expected = self.chrome.find_element(By.XPATH, '//li[contains(text(),"Zip")]').text
        actual = f"The Zip/Postal code you've entered is invalid. It must follow this format: 00000"
        self.assertEqual(expected, actual, 'Not the correct error message')






