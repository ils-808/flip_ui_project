from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class ItemPage:
    def add_to_cart(self):
        with step('Add first available item in list to favorites'):
            browser.element((AppiumBy.ID, 'kz.flip.mobile:id/add_to_cart_btn')).click()

    def check_item_added(self):
        with step('Check item was added successfully'):
            browser.element((AppiumBy.ID, 'kz.flip.mobile:id/go_to_cart_btn')).should(have.text('В КОРЗИНЕ 1 ШТ.'))
