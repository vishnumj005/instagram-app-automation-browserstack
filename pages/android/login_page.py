from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    login_link = (By.ID, "com.instagram.android:id/log_in_button")
    username_input = (By.ID, "com.instagram.android:id/login_username")
    password_input = (By.ID, "com.instagram.android:id/password")
    login_button = (By.ID, "com.instagram.android:id/button_text")

    def click_login_link(self):
        self.click_element(self.login_link)

    def login_to_app(self, username, password):
        self.fill_input(self.username_input, username)\
            .fill_input(self.password_input, password)\
            .click_element(self.login_button)
