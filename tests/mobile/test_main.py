import allure
import pytest

from flip_ui_project_tests.model.mobile.application_manager_mobile import mob_app


@allure.epic('Main page')
class TestMainPage:
    @allure.story('Open main page')
    @allure.title('Product cart opened and added to cart')
    @allure.tag('smoke')
    @allure.label('layer', 'mobile')
    @pytest.mark.mobile
    @pytest.mark.all
    def test_add_first_item_from_suggestion(self):
        mob_app.main_page.open_product_details()
        mob_app.item_page.add_to_cart()

        mob_app.item_page.check_item_added()
