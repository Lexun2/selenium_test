from pages.base_page import Base_page
from selenium.webdriver.common.by import By

class Catalog_page(Base_page):

    url = 'https://shop.a1.by/catalog/c/phones'

    card_smartphones_locator = ( By.CSS_SELECTOR, "img[alt='Смартфоны']" )

    @property
    def card_smartphones(self):
        return self.browser.find_element(*self.card_smartphones_locator)

