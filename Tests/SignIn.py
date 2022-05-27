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
    EMAIL_ADDRESS = (By.ID, 'email')

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
        self.assertTrue = "Invalid email" in error_message
        print("Passed!", error_message)

    def test_forgot_pass_invalid_email(self):
        self.chrome.find_element(*self.FORGOT_PASS).click()
        self.chrome.find_element(*self.EMAIL_ADDRESS).send_keys('george@yahoo.com')
        self.chrome.find_element(*self.RETRIEVE_PASS).click()
        error_message2 = self.chrome.find_element(*self.ERROR_MESSAGE).text
        self.assertTrue = "no account registered" in error_message2
        print("Passed!The error message is: ", error_message2)
