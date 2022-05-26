import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SignIn(unittest.TestCase):
    SIGN_IN = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    FORGOT_PASS = (By.XPATH, '//*[@id="login_form"]/div/p[1]/a')
    RETRIEVE_PASS = (By.XPATH, '//*[@id="form_forgotpassword"]/fieldset/p/button')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="center_column"]/div/div/ol')
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="form_forgotpassword"]/fieldset/div')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.get('http://automationpractice.com/index.php')
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.SIGN_IN).click()

    def tearDown(self):
        self.chrome.quit()

    def test_forgot_pass_error_msg(self):
        self.chrome.find_element(*self.FORGOT_PASS).click()
        self.chrome.find_element(*self.RETRIEVE_PASS).click()
        error_message = self.chrome.find_element(*self.ERROR_MESSAGE).text
        if "Invalid email" in error_message:
            print("Passed!", error_message)
        else:
            print("Test failed!")

    def test_forgot_pass_entered_invalid_email(self):
        self.chrome.find_element(*self.FORGOT_PASS).click()
        email_address = self.chrome.find_element(*self.EMAIL_ADDRESS)
        email_address.click()
        email_address.send_keys('george@george.com')
        email_address.submit()
        error_message = self.chrome.find_element(*self.ERROR_MESSAGE).text
        if "no account registered" in error_message:
            print("Passed!The error message is: ", error_message)
        else:
            print('Test failed!')


