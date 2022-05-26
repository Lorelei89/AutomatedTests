import unittest

import HtmlTestRunner

from Tests.ContactUs import ContactUs


class TestSuite(unittest.TestCase):

    def test_suite_contact_us(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(ContactUs)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='ContactUs',
            report_name='Smoke Test Result'
        )

        runner.run(smoke_test)
