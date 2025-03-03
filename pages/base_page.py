
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from conftest import cookie_accepted


class Base_page:

    url = ''
    cookie_frame_locator         = (By.XPATH,"//div[@role='dialog']/descendant::span[text()='Мы используем файлы cookie']")
    button_accept_cookie_locator = (By.XPATH,"//div[@role='dialog']/descendant::button[text()='Принять']")
    
    def __init__(self, browser):
        self.browser = browser

    def accept_cookie(self):
        global cookie_accepted
        if not cookie_accepted:
            try:
                WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except! не вижу - 'button_accept_cookie_locator'").click
                button_accept_cookie = self.browser.find_element(*self.button_accept_cookie_locator)
                self.browser.execute_script("arguments[0].click();", button_accept_cookie)
                cookie_accepted = True
            except Exception as exc:
                self.browser.execute_script("arguments[0].click();", button_accept_cookie)
                print("Ошибка = {exc}")


        # # try:
            
        #     WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.cookie_frame_locator), "except wait presence 'cookie_frame_locator'")
        #     # time.sleep(100)
        #     button_accept_cookie = self.browser.find_element(*self.button_accept_cookie_locator)
        #     # self.browser.execute_script("arguments[0].click();", button_accept_cookie)
        #     try: WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except wait button 1")
        #     except Exception as exc: print(exc)
        #     try: WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except wait button 2")
        #     except Exception as exc: print(exc)
        #     try: WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except wait button 3")
        #     except Exception as exc: print(exc)
        #     try: WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except wait button 4")
        #     except Exception as exc: print(exc)
        #     try: WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except wait button 5")
        #     except Exception as exc: print(exc)
        #     try: WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except wait button 6")
        #     except Exception as exc: print(exc)
        #     try: WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except wait button 7")
        #     except Exception as exc: print(exc)
        #     try: WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except wait button 8")
        #     except Exception as exc: print(exc)
        #     try: WebDriverWait(self.browser, 1).until(EC.element_to_be_clickable(self.button_accept_cookie_locator), "except wait button 9")
        #     except Exception as exc: print(exc)
        #     self.browser.execute_script("return arguments[0].scrollIntoView(true);", button_accept_cookie)
        #     try:
        #         button_accept_cookie.click()
        #         WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(self.cookie_frame_locator), "except wait not visible 'cookie_frame_locator' 1")
        #     except Exception as exc: print(exc)
        #     try:
        #         button_accept_cookie.click()
        #         WebDriverWait(self.browser, 1).until(EC.invisibility_of_element_located(self.cookie_frame_locator), "except wait not visible 'cookie_frame_locator' 2")
        #     except Exception as exc: print(exc)
        #     try:
        #         button_accept_cookie.click()
        #         WebDriverWait(self.browser, 1).until(EC.invisibility_of_element_located(self.cookie_frame_locator), "except wait not visible 'cookie_frame_locator' 3")
        #     except Exception as exc: print(exc)
        #     try:
        #         button_accept_cookie.click()
        #         WebDriverWait(self.browser, 1).until(EC.invisibility_of_element_located(self.cookie_frame_locator), "except wait not visible 'cookie_frame_locator' 4")
        #     except Exception as exc: print(exc)
        #     try:
        #         button_accept_cookie.click()
        #         WebDriverWait(self.browser, 1).until(EC.invisibility_of_element_located(self.cookie_frame_locator), "except wait not visible 'cookie_frame_locator' 5")
        #     except Exception as exc: print(exc)
        #     try:
        #         button_accept_cookie.click()
        #         WebDriverWait(self.browser, 1).until(EC.invisibility_of_element_located(self.cookie_frame_locator), "except wait not visible 'cookie_frame_locator' 6")
        #     except Exception as exc: print(exc)


        # except Exception as exc:
        #     print(f"Поймали ошибку: {exc}")
        #     self.browser.quit()

    def open(self):
        self.browser.get(self.url)
        self.accept_cookie()
        
    
    