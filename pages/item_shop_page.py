from pages.base_page import Base_page
import time, random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from global_shared import basket


class Item_shop_page(Base_page):

    url = ''
    name = ''
    pay_option = None
    button_credit_radio_list = None
    button_credit_radio = None
    button_credit_locator = ( By.XPATH, "//button/div[contains(text(),'руб/мес частями')]/.." )
    button_credit_radio_list_locator = ( By.XPATH, "//button[@role='radio']" )
    label_name_item_locator = ( By.XPATH, "//h2[@itemprop='name']" )
    button_buy_with_credit_locator = ( By.XPATH, "//div[@role='dialog']/descendant::button[text()='В корзину']" )
    # checked_radio_credit_locator = ( By.XPATH, "//button[@role='radio' and @data-state='checked']" )
    label_credit_month_locator = ( By.XPATH, "//button[@role='radio' and @data-state='checked']/parent::*/parent::*/label" )
    label_credit_paymonth_locator = ( By.XPATH, "//div[@role='radiogroup']/following-sibling::div/div/div/p" )

    def __init__(self, browser, url):
        super().__init__(browser=browser)
        self.url = url
        self.name = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.label_name_item_locator), "except presence label 'name'").text
        self.pay_option = None

    @property
    def button_credit(self):
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.button_credit_locator), "except wait 'credit button'")
        button_credit = self.browser.find_element(*self.button_credit_locator)
        return button_credit
         

    def button_credit_click(self):
        
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", self.button_credit)
        self.button_credit.click()
        time.sleep(1)

    def click_random_credit_radio_button(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.button_credit_radio_list_locator), "except wait 'click_random_credit_radio_button'")
            button_credit_radio_list = self.browser.find_elements(*self.button_credit_radio_list_locator)
            button_credit_radio = button_credit_radio_list[random.randint(1,len(button_credit_radio_list)-1)]
            button_credit_radio.click()
        except:
            print("Печально что через Wait неполучилось нажать на случайный радиобуттон, жмем принудительно скриптом")
            self.browser.execute_script("arguments[0].click();", button_credit_radio)
        time.sleep(1)

    def click_buy_with_credit(self):
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.button_buy_with_credit_locator), "except wait 'button_buy_with_credit_locator'")
        button_buy_with_credit = self.browser.find_element(*self.button_buy_with_credit_locator)
        self.pay_option = self.browser.find_element(*self.label_credit_month_locator).text
        self.label_credit_paymonth = self.browser.find_element(*self.label_credit_paymonth_locator).text
        button_buy_with_credit.click()
        global basket
        basket.add_to_basket(self.name, 1, self.label_credit_paymonth)
        time.sleep(1)
        print(f"Выбран {self.name}, вариант оплаты: {self.pay_option} месяцев, по {self.label_credit_paymonth}")