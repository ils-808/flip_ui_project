from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class MainPage:
    def open_product_details(self):
        with step('Open product details'):
            browser.element((AppiumBy.XPATH,
                             '(//android.widget.FrameLayout[@resource-id="kz.flip.mobile:id/flag_container"])[1]')).click()
