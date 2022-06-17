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
    EMAIL_ADDRESS_REGISTER = (By.XPATH, '//input[@id="email"]')
    EMPTY_EMAIL_ERR = (By.XPATH, '//*[contains(text(),"address required")]')
    SIGN_IN_BTN = (By.XPATH, '//button[@id="SubmitLogin"]')
    PASS_INPUT = (By.XPATH, '//input[@id="passwd"]')
    PASSWORD_ERR = (By.XPATH, '//*[contains(text(),"Invalid password")]')
    EMAIL_CREATE_AC = (By.XPATH, '//input[@id="email_create"]')
    CREATE_AC_BTN = (By.XPATH, '//button[@id="SubmitCreate"]')
    ACCOUNT_EMAIL_ERR = (By.XPATH, '//*[contains(text(),"Invalid")]')
    REGISTER_BTN = (By.XPATH, '//button[@id="submitAccount"]')
    REGISTER_BTN_ERR = (By.XPATH, '//*[contains(text(),"8 errors")]')
    EMPTY_EMAIL_ERR2 = (By.XPATH, '//*[contains(text(),"email address")]')
    BACK_TO_LOGIN_LINK = (By.XPATH, '//a[@title="Back to Login"]')
    AUTH_TITLE = (By.XPATH, '//h1[@class="page-heading"]')
    HOME_ICON = (By.XPATH, '//a[@class="home"]')
    HOME_LOGIN_BTN = (By.XPATH, '//a[@class="login"]')
    LOGO = (By.XPATH, '//img[@class="logo img-responsive"]')
    WOMAN_SECTION = (By.CSS_SELECTOR, '#block_top_menu > ul > li.sfHoverForce > a')
    SECTION_TITLES = (By.XPATH, '//h1[@class="page-heading product-listing"]//parent::span')
    DRESSES_SECTION = (By.CSS_SELECTOR, '#block_top_menu > ul > li:nth-child(2) > a')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.get('http://automationpractice.com/index.php')
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.SIGN_IN).click()

    def tearDown(self):
        self.chrome.quit()

    def test_valid_credentials(self):
        self.chrome.find_element(*self.EMAIL_ADDRESS_REGISTER).send_keys('darkstar_mary@yahoo.com')
        self.chrome.find_element(*self.PASS_INPUT).send_keys('Pass234@#$')
        self.chrome.find_element(*self.SIGN_IN_BTN).click()
        msg = self.chrome.find_element(By.XPATH, '//p[@class="info-account"]').text
        self.assertIn(msg, 'Welcome to your account. Here you can manage all of your personal information and orders.',
                      'Not the correct successfully login text')

    def test_valid_email_no_password_error(self):
        self.chrome.find_element(*self.EMAIL_ADDRESS_REGISTER).send_keys('darkstar_mary@yahoo.com')
        self.chrome.find_element(*self.SIGN_IN_BTN).click()
        msg = self.chrome.find_element(By.XPATH, '//li[contains(text(),"Password")]').text
        self.assertIn(msg, 'Password is required.', 'Not the correct password error')

    def test_failed_login(self):
        self.chrome.find_element(*self.EMAIL_ADDRESS_REGISTER).send_keys('darkstar_mary@yahoo.com')
        self.chrome.find_element(*self.PASS_INPUT).send_keys('aaaaaaaaaaa')
        self.chrome.find_element(*self.SIGN_IN_BTN).click()
        msg = self.chrome.find_element(By.XPATH, '//li[contains(text(),"failed")]').text
        self.assertIn(msg, 'Authentication failed.', 'Not the correct login error')

    def test_forgot_pass_error_msg(self):
        self.chrome.find_element(*self.FORGOT_PASS).click()
        self.chrome.find_element(*self.RETRIEVE_PASS).click()
        error_message = self.chrome.find_element(*self.ERROR_MESSAGE).text
        self.assertTrue = "Invalid email" in error_message
        print("Passed!", error_message)

    def test_forgot_pass_invalid_email(self):
        self.chrome.find_element(*self.FORGOT_PASS).click()
        self.chrome.find_element(*self.EMAIL_ADDRESS_REGISTER).send_keys('george@yahoo.com')
        self.chrome.find_element(*self.RETRIEVE_PASS).click()
        error_message2 = self.chrome.find_element(*self.ERROR_MESSAGE).text
        self.assertTrue = "no account registered" in error_message2
        print("Passed!The error message is: ", error_message2)

    def test_empty_email_input_error(self):
        self.chrome.find_element(*self.EMAIL_ADDRESS_REGISTER).click()
        self.chrome.find_element(*self.SIGN_IN_BTN).click()
        err_msg = self.chrome.find_element(*self.EMPTY_EMAIL_ERR).text
        self.assertIn(err_msg, 'An email address required.', 'Empty email error message not correct!')

    def test_incorrect_password_error(self):
        self.chrome.find_element(*self.EMAIL_ADDRESS_REGISTER).send_keys('nothing@nothing.com')
        self.chrome.find_element(*self.PASS_INPUT).send_keys('aaaa')
        self.chrome.find_element(*self.SIGN_IN_BTN).click()
        pass_err = self.chrome.find_element(*self.PASSWORD_ERR).text
        self.assertIn(pass_err, 'Invalid password.', 'Password error input incorrect')

    def test_empty_create_account_error(self):
        self.chrome.find_element(*self.EMAIL_CREATE_AC).click()
        self.chrome.find_element(*self.CREATE_AC_BTN).click()
        err_msg = self.chrome.find_element(*self.ACCOUNT_EMAIL_ERR).text
        self.assertIn(err_msg, 'Invalid email address.', 'Email error message not correct')

    def test_register_error_msg(self):
        self.chrome.find_element(*self.EMAIL_CREATE_AC).send_keys('mneculau@yahoo.com')
        self.chrome.find_element(*self.CREATE_AC_BTN).click()
        self.chrome.find_element(*self.REGISTER_BTN).click()
        register_err = self.chrome.find_element(*self.REGISTER_BTN_ERR).text
        self.assertIn(register_err, 'There are 8 errors', 'Not the correct register error message')

    def test_sign_in_empty_email_err(self):
        self.chrome.find_element(*self.SIGN_IN_BTN).click()
        email_err_msg = self.chrome.find_element(*self.EMPTY_EMAIL_ERR2).text
        self.assertIn(email_err_msg, 'An email address required.', 'Email error message not correct')

    def test_back_to_login_link(self):
        self.chrome.find_element(*self.FORGOT_PASS).click()
        self.chrome.find_element(*self.BACK_TO_LOGIN_LINK).click()
        expected = self.chrome.find_element(*self.AUTH_TITLE).text
        actual = 'AUTHENTICATION'
        self.assertEqual(expected, actual, 'Incorrect title')

    def test_home_icon_btn(self):
        self.chrome.find_element(*self.HOME_ICON).click()
        expected = self.chrome.find_element(*self.HOME_LOGIN_BTN).text
        actual = 'Sign in'
        self.assertEqual(expected, actual, 'Not the correct signin button')

    def test_logo_sign_in_functionality(self):
        self.chrome.find_element(*self.LOGO).click()
        expected = self.chrome.find_element(*self.HOME_LOGIN_BTN).text
        actual = 'Sign in'
        self.assertEqual(expected, actual, 'Not the correct signin button')

    def test_functionality_woman_section(self):
        self.chrome.find_element(*self.WOMAN_SECTION).click()
        expected = self.chrome.find_element(*self.SECTION_TITLES).text
        actual = 'WOMEN'
        self.assertEqual(expected, actual, 'Not the correct title')

    def test_functionality_dresses_section(self):
        self.chrome.find_element(*self.DRESSES_SECTION).click()
        expected = self.chrome.find_element(*self.SECTION_TITLES).text
        actual = 'DRESSES '
        self.assertEqual(expected, actual, 'Not the correct title')

