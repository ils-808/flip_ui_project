import allure
import pytest

from flip_ui_project_tests.model.mobile.application_manager_mobile import mob_app


@allure.epic('Search Panel')
class TestSearchPanel:
    @allure.story('Search hints')
    @allure.title('After entering search value hints are available')
    @allure.tag('smoke')
    @allure.label('layer', 'mobile')
    @pytest.mark.mobile
    @pytest.mark.all
    @pytest.mark.parametrize('value,amount', [('iphone 13', 3)])
    def test_hints_available_after_entering_item_name(self, value, amount):
        mob_app.search_panel.tap_on_icon()
        mob_app.search_panel.search(value)
        mob_app.search_panel.check_search_hints(amount)
