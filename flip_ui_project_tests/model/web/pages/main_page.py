from selene import browser, be
from allure import step


class MainPage:
    def open_main_page(self):
        with step('Open main page'):
            browser.open('/')

    def catalog_menu_should_be_visible(self):
        with step('Burger menu is visible'):
            browser.element('header > div.menu.cell.hover-affect > div > p').should(be.visible)

    def slide_show_should_be_visible(self):
        with step('Banner carousel is visible'):
            browser.element('td>.slideshow-container').should(be.visible)
