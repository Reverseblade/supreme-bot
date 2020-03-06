from urllib.request import urlopen
from urllib.error import HTTPError

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

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

    def watch_release(self):
        print('Started watching release..')

        while(True):
            if self.check_release():
                print('Release detected')
                break
            else:
                print('Release not detected')
                sleep(2)

    def check_release(self):
        try:
            html = urlopen("https://www.supremenewyork.com/shop/all")
        except HTTPError as e:
            print(e)
        try:
            bs = BeautifulSoup(html.read(),'html.parser')
            first_product = bs.find("a", href=self.products[0]['href'])
            if first_product:
                return True
            else:
                return False
        except AttributeError as e:
            print(e)

    def run(self):

        if WATCH_MODE:
            self.watch_release()

        option = Options()

        if PROXY:
            option.add_argument('--proxy-server=http://%s' % PROXY)

        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=option)
        driver.set_window_position(self.window_position_x, self.window_position_y)
        driver.set_window_size(self.window_width, self.window_height)

        shop_all_page = ShopAllPage(driver)
        shop_all_page.open()

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

        sleep(MANUAL_ADJUSTMENT_TIME)
