from selene import browser, have
from allure import step


class ItemPage:
    def check_product_name_in_table(self, item_name):
        with step(f'Check that {item_name} matches'):
            browser.element('td>h1').should(have.text(item_name))

    def check_product_name_in_div(self, item_name):
        with step(f'Check that {item_name} matches'):
            browser.element('.main_left_top_middle_right').element('h1').should(have.text(item_name))
