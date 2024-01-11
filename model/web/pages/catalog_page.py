from allure_commons._allure import step
from selene import browser, have, be


class CatalogPage:
    def click_on_item(self, item_name):
        with step(f'Go to item {item_name} from catalog'):
            browser.all('.table>.info>.title').element_by(have.exact_text(item_name)).click()

    def check_product_name(self, item_name):
        with step(f'Check is present'):
            browser.all('.info>.title').element_by(have.exact_text(item_name)).should(be.visible)

    def check_add_to_cart_modal_window(self, item_name):
        with step(f'Add to cart {item_name}'):
            browser.all('.table>.info>.title').element_by(have.exact_text(item_name)).hover()
            browser.all('.btn-add').element_by(be.visible).click()
            browser.element('.loaded').should(have.text('Товар добавлен в корзину'))

    def close_popup_cart(self):
        with step('Close popup'):
            browser.element('.gray.close_button').click()
