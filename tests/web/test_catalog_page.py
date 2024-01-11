import allure
import pytest

from model.web.application_manager import app


@allure.epic('Catalog page')
class TestCatalogPage:
    @allure.story('Open catalog page')
    @allure.title('Iteml should be shown')
    @allure.tag('smoke')
    @allure.label('layer', 'web')
    @pytest.mark.web
    @pytest.mark.all
    @pytest.mark.parametrize('first_category,second_category,item_name',
                             [('Продукты питания', 'Чай', 'Чай травяной с кедровой шишкой')])
    def test_open_catalog(self, first_category, second_category, item_name):
        app.main_page.open_main_page()
        app.menu_panel.go_to_third_category_menu(first_category, second_category)

        app.catalog_page.check_product_name(item_name)

    @allure.story('Open catalog page')
    @allure.title('Modal window after click \'Add to cart\' should be shown')
    @allure.tag('smoke')
    @allure.label('layer', 'web')
    @pytest.mark.web
    @pytest.mark.all
    @pytest.mark.parametrize('first_category,second_category,item_name',
                             [('Продукты питания', 'Чай', 'Чай белый пакетированный')])
    def test_add_to_cart_catalog(self, first_category, second_category, item_name):
        app.main_page.open_main_page()
        app.menu_panel.go_to_third_category_menu(first_category, second_category)

        app.catalog_page.check_add_to_cart_modal_window(item_name)

    @allure.story('Open catalog page')
    @allure.title('After adding item to cart it should be shown in Cart Page')
    @allure.tag('smoke')
    @allure.label('layer', 'web')
    @pytest.mark.web
    @pytest.mark.all
    @pytest.mark.parametrize('first_category,second_category,item_name',
                             [('Продукты питания', 'Чай', 'Чай белый пакетированный')])
    def test_added_item_in_cart(self, first_category, second_category, item_name):
        app.main_page.open_main_page()
        app.menu_panel.go_to_third_category_menu(first_category, second_category)
        app.catalog_page.check_add_to_cart_modal_window(item_name)
        app.catalog_page.close_popup_cart()
        app.cart_panel.go_to_cart()

        app.cart_panel.check_item_name(item_name)
