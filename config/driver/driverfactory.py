import json

from appium import webdriver
import os


class DriverFactory(object):
    def __init__(self, context):
        self.driver_config = {}
        self.desired_capabilities = None
        self.environment = context.env
        self.platform = context.platform

    def start_driver(self, context):
        context.driver = getattr(self, self.environment)()
        context.platform = self.desired_capabilities['platformName']

        if self.platform == 'Android':
            from pages.android.login_page import LoginPage
        elif self.platform == 'iOS':
            from pages.ios.login_page import LoginPage
        else:
            raise RuntimeError(f'Unrecognized platform: {context.platform}')
        context.login_page = LoginPage(context)

    def mobile(self):
        driver = webdriver.Remote(
            command_executor='http://%s:%s/wd/hub' % (self.driver_config.get('host'), self.driver_config.get('port')),
            desired_capabilities=self.desired_capabilities
        )

        return driver

    def browserstack(self):
        driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor="http://%s:%s@hub.browserstack.com/wd/hub" % (
                self.driver_config['browserstack_user'], self.driver_config['browserstack_key'])
        )

        return driver

    def driver_setup(self, context):
        if self.environment == 'browserstack':
            config_file_path = os.getcwd() + os.path.sep + "config/browserstack.json"
        else:
            config_file_path = os.getcwd() + os.path.sep + "config/mobilecapabilities.json"

        with open(config_file_path) as config_file:
            CONFIG = json.load(config_file)

        if self.platform == 'Android':
            self.desired_capabilities = CONFIG['Android']
        else:
            self.desired_capabilities = CONFIG['iOS']

        context.app_url = self.desired_capabilities['app']

        self.driver_config['browserstack_user'] = context.config.userdata['user']
        self.driver_config['browserstack_key'] = context.config.userdata['key']
        self.driver_config['host'] = context.config.userdata['appium_host']
        self.driver_config['port'] = context.config.userdata['appium_port']

