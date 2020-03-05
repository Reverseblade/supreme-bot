from time import sleep

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Locators import ShopPageLocator
from Locators import ShopAllPageLocator
from Locators import ProductPageLocator
from Locators import CheckoutPageLocator

from config import *

class BasePage:

    def __init__(self, driver=None, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()


class ShopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url='https://www.supremenewyork.com/shop/')

    def shop_all(self):
        locator = ShopPageLocator.shop_all
        shop_all = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        shop_all.click()


class ShopAllPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url='https://www.supremenewyork.com/shop/all')

    def click_product(self, href):
        locator = (By.XPATH, '//a[@href="' + href + '"]')
        target_product = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        target_product.click()
    

class ProductPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver=driver)

    def select_size(self, text):
        locator = ProductPageLocator.size_select_box
        wait = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        size_select_box = Select(wait)
        size_select_box.select_by_visible_text(text)

    def add_to_cart(self):
        locator = ProductPageLocator.add_btn
        add_btn = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        add_btn.click()

    def checkout(self):
        locator = ProductPageLocator.checkout_btn
        checkout_btn = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        checkout_btn.click()

    def shop_all(self):
        locator = ProductPageLocator.shop_all
        shop_all = self.driver.find_element(*locator)
        shop_all.click()

class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def fillout(self):
        """
        お届け先・支払い情報の入力
        """

        # 名前
        locator = CheckoutPageLocator.name
        name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        name.send_keys(CHECKOUT_INFO['name'])

        sleep(FILL_OUT_DELAY)

        # Eメール
        locator = CheckoutPageLocator.email
        email = self.driver.find_element(*locator)
        email.send_keys(CHECKOUT_INFO['email'])

        sleep(FILL_OUT_DELAY)

        # 電話番号
        locator = CheckoutPageLocator.phone_number
        phone_number = self.driver.find_element(*locator)
        phone_number.send_keys(CHECKOUT_INFO['phone_number'])

        sleep(FILL_OUT_DELAY)

        # 郵便番号
        locator = CheckoutPageLocator.zip_code
        zip_code = self.driver.find_element(*locator)
        zip_code.send_keys(CHECKOUT_INFO['zip_code'])

        sleep(FILL_OUT_DELAY)

        # 都道府県
        locator = CheckoutPageLocator.billing_state
        billing_state = Select(self.driver.find_element(*locator))
        billing_state.select_by_visible_text(CHECKOUT_INFO['billing_state'])

        sleep(FILL_OUT_DELAY)

        # 区市町村
        locator = CheckoutPageLocator.billing_city
        billing_city = self.driver.find_element(*locator)
        billing_city.clear()
        billing_city.send_keys(CHECKOUT_INFO['billing_city'])

        sleep(FILL_OUT_DELAY)

        # 住所
        locator = CheckoutPageLocator.billing_address
        billing_address = self.driver.find_element(*locator)
        billing_address.send_keys(CHECKOUT_INFO['billing_address'])

        sleep(FILL_OUT_DELAY)

        # この住所を保存する
        locator = CheckoutPageLocator.store_address_check_box
        store_address_check_box = self.driver.find_element(*locator)
        store_address_check_box.click()

        sleep(FILL_OUT_DELAY)

        # 支払い方法
        locator = CheckoutPageLocator.card_type_select_box
        card_type = Select(self.driver.find_element(*locator))
        card_type.select_by_visible_text(CHECKOUT_INFO['card_type'])

        sleep(FILL_OUT_DELAY)

        # カード番号
        locator = CheckoutPageLocator.card_number
        card_number = self.driver.find_element(*locator)
        card_number.send_keys(CHECKOUT_INFO['card_number'])

        sleep(FILL_OUT_DELAY)

        # 有効期限(月) 
        locator = CheckoutPageLocator.card_month_select_box
        card_month_select_box = Select(self.driver.find_element(*locator))
        card_month_select_box.select_by_value(CHECKOUT_INFO['card_month'])

        sleep(FILL_OUT_DELAY)

        # 有効期限（年）
        locator = CheckoutPageLocator.card_year_select_box
        card_year_select_box = Select(self.driver.find_element(*locator))
        card_year_select_box.select_by_value(CHECKOUT_INFO['card_year'])

        sleep(FILL_OUT_DELAY)

        # CSV番号
        locator = CheckoutPageLocator.card_cvv
        card_cvv = self.driver.find_element(*locator)
        card_cvv.send_keys('1234')

        sleep(FILL_OUT_DELAY)

        # 利用規約同意
        locator = CheckoutPageLocator.agreement_check_box
        agreement_check_box = self.driver.find_element(*locator)
        agreement_check_box.click()

        sleep(FILL_OUT_DELAY)

    def process_payment(self):
        """
        購入する
        """
        locator = CheckoutPageLocator.process_payment
        process_payment = self.driver.find_element(*locator)
        process_payment.click()
