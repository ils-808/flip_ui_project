from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from allure import step


class HeaderComponent:
    def open_burger_menu(self):
        with step('Open burger menu'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()

    def go_to_auth(self):
        with step('Open auth page'):
            browser.element(
                (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="kz.flip.mobile:id/login_btn"]')).click()
