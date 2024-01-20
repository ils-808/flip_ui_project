from selene import browser, have
from allure import step


class CartComponent:
    def go_to_cart(self):
        with step(f'Go to cart'):
            browser.element('#w_cart > .table').click()

    def check_item_name(self, item_name):
        with step(f'Item name in cart should be same {item_name}'):
            browser.element('.table>.cell .p-20>b>a').should(have.text(item_name))
