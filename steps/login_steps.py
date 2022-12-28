from behave import step

from config.constants.authentication import Authentication


@step("user clicks login link")
def step_impl(context):
    context.login_page.click_login_link()


@step("user attempts to login with valid credentials")
def step_impl(context):
    context.login_page.login_to_app(Authentication.USERNAME, Authentication.PASSWORD)
