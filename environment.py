from config.driver.driverfactory import DriverFactory


def before_all(context):
    context.env = context.config.userdata['env']
    context.platform = context.config.userdata['platform']

    driver_factory = DriverFactory(context)
    driver_factory.driver_setup(context)
    driver_factory.start_driver(context)


def after_all(context):
    context.driver.remove_app(context.app_url)
