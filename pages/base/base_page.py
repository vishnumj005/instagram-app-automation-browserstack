from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import config.base_config as config


class BasePage(object):

    def __init__(self, context):
        self.driver = context.driver
        self.timeout = config.default_wait
        self.context = context

    def find_element(self, locator, timeout=config.default_wait):
        try:
            return WebDriverWait(self.driver, timeout=timeout).until(ec.visibility_of_element_located(locator),
                                                                      'ELEMENT IS NOT FOUND OR VISIBLE! => {}'.format(
                                                                          locator))
        except TimeoutException as e:
            error = e.args[0]
            raise TimeoutException(error) from e.__cause__

    def click_element(self, locator, timeout=config.default_wait):
        try:
            WebDriverWait(self.driver, timeout=timeout).until(ec.presence_of_element_located(locator),
                                                              'UNABLE TO LOCATE ELEMENT! => {}'.format(
                                                                  locator)).click()
        except TimeoutException as e:
            error = e.args[0]
            raise TimeoutException(error) from e.__cause__
        return self

    def fill_input(self, locator, value):
        element = self.find_element(locator)
        element.send_keys(value)
        return self

    def install_app(self, context):
        if context.env == 'mobile':
            self.driver.install_app(context.app_url)
