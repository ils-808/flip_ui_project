import allure
import pytest

from model.web.application_manager import app


@allure.epic('Search page')
class TestSearchPage:
    @allure.story('Search item')
    @allure.title('Item should be found')
    @allure.tag('smoke')
    @allure.label('layer', 'web')
    @pytest.mark.parametrize('item_search', ['Атомные привычки'])
    @pytest.mark.web
    @pytest.mark.all
    def test_item_search(self, item_search):
        app.main_page.open_main_page()
        app.search_panel.type_then_search(item_search)

        app.catalog_page.check_product_name(item_search)
