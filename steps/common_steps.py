from behave import step

from pages.base.base_page import BasePage


@step("app is launched")
def step_impl(context):
    BasePage(context).install_app(context)
