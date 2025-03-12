
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from conftest import cookie_accepted
from selenium.webdriver.common.action_chains import ActionChains
import time

class Base_page:

    url = ''
    cookie_frame_locator         = (By.XPATH,"//div[@role='dialog']/descendant::span[text()='Мы используем файлы cookie']")
    button_accept_cookie_locator = (By.XPATH,"//div[@role='dialog']/descendant::button[text()='Принять']")
    
    

    def __init__(self, browser):
        self.browser = browser



    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    


    def open(self):
        self.browser.get(self.url)
        self.accept_cookie()




    def accept_cookie(self):
        global cookie_accepted
        if not cookie_accepted:
            try:  
                while (self.is_element_present(*self.cookie_frame_locator)):
                    button_accept_cookie = WebDriverWait(self.browser, 50).until(EC.visibility_of_element_located(self.button_accept_cookie_locator), "except! не вижу - 'button_accept_cookie_locator'")
                    actions = ActionChains(self.browser)
                    actions.move_to_element(button_accept_cookie).perform()
                    actions.click().perform()
                    time.sleep(1)
                cookie_accepted = True
            except Exception as exc:
                print(f"Ошибка по принятию соглашения кукисов = {exc}")



        
    
    