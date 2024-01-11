from model.mobile.components.header_panel import HeaderComponent
from model.mobile.components.search_panel import SearchComponent
from model.mobile.pages.auth_page import AuthPage
from model.mobile.pages.item_page import ItemPage
from model.mobile.pages.main_page import MainPage


class MobileApplication:
    def __init__(self):
        self.main_page = MainPage()
        self.item_page = ItemPage()
        self.auth_page = AuthPage()

        self.header_panel = HeaderComponent()
        self.search_panel = SearchComponent()


mob_app = MobileApplication()
