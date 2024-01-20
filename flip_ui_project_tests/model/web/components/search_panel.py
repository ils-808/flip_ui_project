from selene import browser
from allure import step


class SearchComponent:
    def type_then_search(self, text_to_find):
        with step(f'Ввод значения {text_to_find}'):
            browser.element('#search_input').send_keys(text_to_find).submit()
