from typing import Literal

import pydantic_settings
import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from utils import attach
from utils.resource_handler import path

BrowserType = Literal['chrome', 'firefox']


class Configure(pydantic_settings.BaseSettings):
    context: Literal['local', 'remote'] = 'local'
    base_url: str = 'https://www.flip.kz'
    height: str = '1080'
    width: str = '1920'
    timeout: float = 10.0
    browser: BrowserType = 'chrome'
    version: str = '119'
    login: str = 'dummy_value'
    password: str = 'dummy_value'
    remote_browser_url: str = 'dummy_value'


config = Configure(_env_file=path(f'.env.{Configure().context}'))


@pytest.fixture(scope='function', autouse=True)
def configure_browser():
    options = Options()
    if config.context == 'remote':
        selenoid_capabilities = {
            'browserName': config.browser,
            'browserVersion': config.version,
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        options.add_argument(f'--window-size={config.width},{config.height}')

        # driver = webdriver.Remote(
        #     command_executor=f"https://{config.login}:{config.password}@{config.remote_browser_url}",
        #     options=options
        # )
        driver = webdriver.Remote(
            command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options
        )
        browser.config.driver = driver
    else:
        browser.config.driver_name = config.browser
        options.add_argument('--ignore-certificate-errors')
        browser.config.driver_options = options
        browser.config.window_width = config.width
        browser.config.window_height = config.height

    browser.config.base_url = config.base_url

    yield

    attach.add_screenshot(browser)
    attach.add_html(browser)
    if config.browser == 'chrome':
        attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()