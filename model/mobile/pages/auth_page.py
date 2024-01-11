from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class AuthPage:
    def enter_login(self, phone_number):
        with step(f'Enter phone-number {phone_number}'):
            browser.element((AppiumBy.ID, 'kz.flip.mobile:id/phone_et')).send_keys(phone_number)
        with step('Click on Login button'):
            browser.element((AppiumBy.ID, 'kz.flip.mobile:id/login_btn')).click()

    def check_sms_popup(self):
        with step('SMS popup should be shown'):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup')).should(
                be.visible)
