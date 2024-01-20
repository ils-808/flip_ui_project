from flip_ui_project_tests.model.web.components.cart_panel import CartComponent
from flip_ui_project_tests.model.web.components.menu_panel import MenuComponent
from flip_ui_project_tests.model.web.components.search_panel import SearchComponent
from flip_ui_project_tests.model.web.pages.catalog_page import CatalogPage
from flip_ui_project_tests.model.web.pages.item_page import ItemPage
from flip_ui_project_tests.model.web.pages.main_page import MainPage


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.catalog_page = CatalogPage()
        self.item_page = ItemPage()
        self.search_panel = SearchComponent()

        self.menu_panel = MenuComponent()
        self.cart_panel = CartComponent()


app = Application()
