from urllib.request import urlopen, ProxyHandler, build_opener, install_opener
from urllib.error import HTTPError
import urllib.request
import logging
import sys
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

from pages import ShopPage, ShopAllPage, ProductPage, CheckoutPage
from time import sleep
from config import *

formatter = '%(asctime)s: %(message)s'
filename = 'logs/main.log'
logging.basicConfig(level=logging.INFO, filename=filename, format=formatter)

class Task:
    def __init__(self, products, process_count):
        self.products = products

        self.window_width = 1000
        self.window_height = 900
        self.window_position_x = self.window_width/2 * process_count - 50
        self.window_position_y = 0

    def watch_release(self):
        logging.info('Waiting for the new items to drop')

        while(True):
            if self.check_release():
                logging.info('Drop detected')
                break
            else:
                logging.info('Drop not detected')
                sleep(2)

    def check_release(self):
        new_product = self.products[0]
        return self.check_product_existance(new_product)

    def check_product_existance(self, product):
        try:
            if PROXY:
                proxies ={'https':PROXY}
                proxy_handler = urllib.request.ProxyHandler(proxies)
                opener = urllib.request.build_opener(proxy_handler)
                urllib.request.install_opener(opener)
            html = urllib.request.urlopen("https://www.supremenewyork.com/shop/all")
        except HTTPError as e:
            logging.error(e)
        try:
            bs = BeautifulSoup(html.read(),'html.parser')
            product = bs.find("a", href=product['href'])
            if product:
                return True
            else:
                return False
        except AttributeError as e:
            logging.error(e)
            return False

    def check_stock(self, product):
        try:
            if PROXY:
                proxies ={'https':PROXY}
                proxy_handler = urllib.request.ProxyHandler(proxies)
                opener = urllib.request.build_opener(proxy_handler)
                urllib.request.install_opener(opener)
            html = urlopen('https://www.supremenewyork.com' + product['href'])
        except HTTPError as e:
            logging.error(e)
        try:
            bs = BeautifulSoup(html.read(),'html.parser')
            is_sold_out = bs.find('b', class_='sold-out')
            if is_sold_out is None:
                return True
            else:
                return False
        except AttributeError as e:
            logging.error(e)
            return False
        
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
            if not self.check_product_existance(product):
                logging.info('Product "' + product['name'] + '" not found')
                continue
            elif not self.check_stock(product):
                logging.info('Product "' + product['name'] + '" is sold out')
                continue
            else: 
                logging.info('Product "' + product['name'] + '" is in stock')

                shop_all_page.click_product(product['href'])
                product_page = ProductPage(shop_all_page.driver)
                if product['size'] is not None:
                    product_page.select_size(product['size'])
                product_page.add_to_cart()
                sleep(ADD_TO_CART_DELAY)

                logging.info(f'Product "{product["name"]}" is added to cart')

                if i == len(self.products) - 1:
                    product_page.checkout()
                    checkout_page = CheckoutPage(product_page.driver)
                    checkout_page.fillout()
                    logging.info('Checkout info filled out')
                    # if AUTO_PROCESS_PAYMENT:
                    #     checkout_page.process_payment()
                else:
                    product_page.shop_all()
                    shop_all_page = ShopAllPage(product_page.driver)

                sleep(MANUAL_ADJUSTMENT_TIME)
