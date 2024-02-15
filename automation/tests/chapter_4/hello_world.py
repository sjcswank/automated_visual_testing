from automation.tests.base_test import BaseTest
from selenium.webdriver.common.by import By



class HelloWorldTest(BaseTest):

    def test_hello_world(self):
        self.set_up(test_name=self._testMethodName)
        self.validate_window(tag='hello_world')
        self.driver.find_element(By.CSS_SELECTOR, 'button').click()
        self.validate_window(tag='click_me')

        self.teardown()

