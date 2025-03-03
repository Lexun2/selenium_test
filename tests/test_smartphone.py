from pages.smartphones_page import Smartphones_page
from pages.item_shop_page import Item_shop_page
import time
from global_shared import basket
from conftest import start_time

def test_smartphone(browser):
    global basket
    global start_time
    smartphones_page = Smartphones_page(browser)
    smartphones_page.open()
    time.sleep(2)
    smartphones_page.check_random_smartphone_card()
    time.sleep(1)
    item_shop_page = Item_shop_page(browser, browser.current_url)
    item_shop_page.button_credit_click()
    time.sleep(1)
    item_shop_page.click_random_credit_radio_button()
    item_shop_page.click_buy_with_credit()
    smartphones_page.open()
    smartphones_page.check_random_smartphone_card()
    item_shop_page2 = Item_shop_page(browser, browser.current_url)
    item_shop_page2.button_credit_click()
    item_shop_page2.click_random_credit_radio_button()
    item_shop_page2.click_buy_with_credit()
    for el in basket.products:
        print(f"\nВ корзине лежит: {el[0]}  -  {el[1]} шт., опция оплаты: {el[2]}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"На выполнение теста выбора телефона и способа его оплаты в кредит ушло {elapsed_time:.2f} секунд.")