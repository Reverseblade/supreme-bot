from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import ShopPage, ShopAllPage, ProductPage, CheckoutPage
from time import sleep
from config import *
from selenium.webdriver.support.ui import Select


class Task:
    def __init__(self, products, process_count):
        self.products = products

        self.window_width = 1000
        self.window_height = 900
        self.window_position_x = self.window_width/2 * process_count - 50
        self.window_position_y = 0

    def run(self):

        option = Options()

        if PROXY:
            option.add_argument('--proxy-server=http://%s' % self.proxy)

        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=option)
        driver.set_window_position(self.window_position_x, self.window_position_y)
        driver.set_window_size(self.window_width, self.window_height)

        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.shop_all()

        shop_all_page = ShopAllPage(shop_page.driver)

        for i, product in enumerate(self.products):
            shop_all_page.click_product(product['href'])
            product_page = ProductPage(shop_all_page.driver)
            if product['size'] is not None:
                product_page.select_size(product['size'])
            product_page.add_to_cart()
            sleep(ADD_TO_CART_DELAY)

            if i == len(self.products) - 1:
                product_page.checkout()
                checkout_page = CheckoutPage(product_page.driver)
                checkout_page.fillout()
                # if AUTO_PROCESS_PAYMENT:
                #     checkout_page.process_payment()
            else:
                product_page.shop_all()
                shop_all_page = ShopAllPage(product_page.driver)

        # 手動調整用の時間
        sleep(9999)

