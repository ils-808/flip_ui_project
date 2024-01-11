from selene import browser, have
from allure import step


class MenuComponent:
    def go_to_third_category_menu(self, parent_categroy, child_category):
        with step(f'Open category {parent_categroy}'):
            browser.element('.menu.cell').hover().all('.cell.p-r-8').element_by(
                have.exact_text(parent_categroy)).hover()

        with step(f'Click on category {child_category}'):
            browser.all('.sub-new>.column>ul>li>.title').element_by(
                have.exact_text(child_category)).click()
