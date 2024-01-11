import allure
import pytest

from model.mobile.application_manager_mobile import mob_app
from model.web.application_manager import app


@allure.epic('Auth page')
class TestAuthPage:
    @allure.story('Open auth page')
    @allure.title('After entering phone-number SMS popup is available')
    @allure.tag('smoke')
    @allure.label('layer', 'mobile')
    @pytest.mark.mobile
    @pytest.mark.all
    @pytest.mark.parametrize('phone_number', ['77017386004'])
    def test_item_added(self, phone_number):
        mob_app.header_panel.open_burger_menu()
        mob_app.header_panel.go_to_auth()
        mob_app.auth_page.enter_login(phone_number)

        mob_app.auth_page.check_sms_popup()
