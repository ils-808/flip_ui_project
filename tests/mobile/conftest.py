import allure
import allure_commons
import pytest
from appium import webdriver
from config import loaded_configuration
from flip_ui_project_tests.utils import attach

from appium.options.android import UiAutomator2Options
from selene import browser, support

from flip_ui_project_tests.utils.resource_handler import get_path


@pytest.fixture(scope='function', autouse=True)
def configure_mobile_browser():
    options = UiAutomator2Options()

    options.set_capability('deviceName', loaded_configuration.deviceName)
    options.set_capability('app', (
        loaded_configuration.app if loaded_configuration.app.startswith('/') or loaded_configuration.app.startswith(
            'bs://')
        else get_path(loaded_configuration.app)
    ))
    options.set_capability('appium:autoGrantPermissions', True)

    if loaded_configuration.context == 'remote':
        options.set_capability('platformVersion', loaded_configuration.platformVersion)
        options.set_capability(
            'bstack:options', {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",

                # Set your access credentials
                "userName": loaded_configuration.login,
                "accessKey": loaded_configuration.password,
            }
        )

    configure_browser(options)

    yield

    attach.add_screenshot()
    with allure.step('Tear down app session'):
        browser.quit()
    if loaded_configuration.context == 'remote':
        attach.attach_bstack_video(browser.driver.session_id)


def configure_browser(options):
    with allure.step('Init app session'):
        browser.config.driver = webdriver.Remote(
            loaded_configuration.server_url,
            options=options)
        browser.config.timeout = loaded_configuration.timeout

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)
