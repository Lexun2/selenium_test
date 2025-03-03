import pytest, time
from selenium import webdriver
# from fake_useragent import UserAgent
# from pages.basket_shop import Basket_shop

# def get_random_chrome_user_agent():
#     user_agent = UserAgent(browsers='chrome', os='windows', platforms='pc')
#     return user_agent.random
start_time = time.time()
cookie_accepted = False

@pytest.fixture
def browser():
    try:
        options = webdriver.ChromeOptions()
        # options.page_load_strategy = 'normal'   # eager normal none
        # assert options.capabilities['browserName'] == 'chrome'
        options.add_argument('log-level=1') # Допустимые значения от 0 до 3:        # INFO = 0,       # WARNING = 1,      # LOG_ERROR = 2,        # LOG_FATAL = 3.
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--allow-insecure-localhost')
        options.add_argument('disable-quic')
        
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
        yield browser
    finally: 
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nНа выполнение данной сессии тестирования {elapsed_time:.2f} секунд.")
        browser.quit()

# @pytest.fixture(scope = "session", Autouse=True)
# def start():
#     global basket_shop
#     basket_shop = Basket_shop()