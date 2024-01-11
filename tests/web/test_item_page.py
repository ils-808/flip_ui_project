import allure
import pytest

from model.web.application_manager import app


@allure.epic('Item page')
class TestItemPage:
    @allure.story('Open item page')
    @allure.title('Item name should be shown')
    @allure.tag('smoke')
    @allure.label('layer', 'web')
    @pytest.mark.web
    @pytest.mark.all
    @pytest.mark.parametrize('first_category,second_category,item_name',
                             [('Книги', 'Художественная литература', 'Шах и мат')])
    def test_open_item_page(self, first_category, second_category, item_name):
        app.main_page.open_main_page()
        app.menu_panel.go_to_third_category_menu(first_category, second_category)
        app.catalog_page.click_on_item(item_name)

        app.item_page.check_product_name_in_table(item_name)
