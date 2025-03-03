from pages.base_page import Base_page
from selenium.webdriver.common.by import By
import random, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Smartphones_page(Base_page):
    __instance = None
    url = 'https://shop.a1.by/catalog/phones/smartphones'
    list_smartphones_locator = ( By.XPATH, "//div[@itemprop='itemListElement']" )
    

    def __new__(cls, *args, **kwargs):
        if   cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Smartphones_page.__instance = None

    @property
    def list_smartphones(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.list_smartphones_locator), "except wait 'list_smartphones_locator'")
        return self.browser.find_elements(*self.list_smartphones_locator)
    

    def check_random_smartphone_card(self):
        phone_card = self.list_smartphones[random.randint(1,len(self.list_smartphones)-1)]
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", phone_card)
        try:
            WebDriverWait(self.browser, 100).until(EC.element_to_be_clickable(phone_card), "except wait clickable 'list_smartphones_locator'").click()
        except:
            print("Жму принудительно на выбор случайного смартфона")
            self.browser.execute_script("arguments[0].click();", phone_card)
    
