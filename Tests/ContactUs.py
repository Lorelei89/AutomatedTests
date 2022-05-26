import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ContactUs(unittest.TestCase):
    CONTACT_US = (By.XPATH, '//*[@id="contact-link"]/a')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submitMessage"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="center_column"]/div/ol/li')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.get('http://automationpractice.com/index.php')
        self.chrome.implicitly_wait(30)
        self.chrome.find_element(*self.CONTACT_US).click()

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'http://automationpractice.com/index.php?controller=contact'
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_page_title(self):
        actual = self.chrome.title
        expected = 'CUSTOMER SERVICE - CONTACT US'
        self.assertEqual(expected, actual, 'Page title is incorrect')
