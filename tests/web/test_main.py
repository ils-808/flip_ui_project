import allure
import pytest

from flip_ui_project_tests.model.web.application_manager import app


@allure.epic('Main page')
class TestMainPage:
    @allure.story('Open main page')
    @allure.title('Catalog menu should be shown')
    @allure.tag('smoke')
    @allure.label('layer', 'web')
    @pytest.mark.web
    @pytest.mark.all
    def test_menu_present(self):
        app.main_page.open_main_page()

        app.main_page.catalog_menu_should_be_visible()

    @allure.story('Open main page')
    @allure.title('Banner carousel should be shown')
    @allure.tag('smoke')
    @allure.label('layer', 'web')
    @pytest.mark.web
    @pytest.mark.all
    def test_banner_carousel_present(self):
        app.main_page.open_main_page()

        app.main_page.slide_show_should_be_visible()
