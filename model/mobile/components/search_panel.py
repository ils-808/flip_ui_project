from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from allure import step


class SearchComponent:
    def tap_on_icon(self):
        with step('Click on search icon'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Поиск')).click()

    def search(self, value):
        with step(f'Search {value}'):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.AutoCompleteTextView[@resource-id="kz.flip.mobile:id/search_edit_text"]')).send_keys(
                value)

    def check_search_hints(self, amonunt):
        with step(f'Check search hints should be shown at least {amonunt}'):
            browser.all((AppiumBy.ID, 'kz.flip.mobile:id/suggestion_text')).should(
                have.size_greater_than_or_equal(amonunt))
