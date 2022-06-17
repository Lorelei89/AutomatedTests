import unittest

import HtmlTestRunner

from Tests.Cart import Cart
from Tests.ContactUs import ContactUs
from Tests.SignIn import SignIn


class TestSuite(unittest.TestCase):

    def test_suite_contact_us(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(ContactUs)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Contact Us',
            report_name='Smoke Test Result'
        )

        runner.run(smoke_test)

    def test_suite_sing_in(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SignIn)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Sign In',
            report_name='Sign In test results'
        )
        runner.run(smoke_test)

    def test_suite_cart(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Cart)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Cart',
            report_name='Cart test results'
        )
        runner.run(smoke_test)