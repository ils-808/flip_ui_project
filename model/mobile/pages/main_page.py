from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class MainPage:
    def open_product_details(self):
        with step('Add first available item in list to favorites'):
            browser.element((AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="kz.flip.mobile:id/flag_container"])[1]')).click()
