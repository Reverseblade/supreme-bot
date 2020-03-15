from time import sleep

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Locators import *
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
        shop_all = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        shop_all.click()


class ShopAllPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url='https://www.supremenewyork.com/shop/all')

    def click_product(self, href):
        locator = (By.XPATH, '//a[@href="' + href + '"]')
        target_product = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        target_product.click()
    

class ProductPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver=driver)

    def select_size(self, text):
        locator = ProductPageLocator.size_select_box
        wait = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        size_select_box = Select(wait)
        size_select_box.select_by_visible_text(text)

    def add_to_cart(self):
        locator = ProductPageLocator.add_btn
        add_btn = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        add_btn.click()

    def checkout(self):
        locator = ProductPageLocator.checkout_btn
        checkout_btn = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(locator))
        checkout_btn.click()

    def shop_all(self):
        locator = ProductPageLocator.shop_all
        shop_all = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        shop_all.click()

class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def fillout(self):
        """
        お届け先・支払い情報の入力
        """

        # 名前
        locator = MobileMobileCheckoutPageLocator.name
        name = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(locator))
        name.clear()
        name.send_keys(CHECKOUT_INFO['name'])

        sleep(FILL_OUT_DELAY)

        # Eメール
        locator = MobileMobileCheckoutPageLocator.email
        email = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        email.send_keys(CHECKOUT_INFO['email'])

        sleep(FILL_OUT_DELAY)

        # 電話番号
        locator = MobileMobileCheckoutPageLocator.phone_number
        phone_number = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        phone_number.send_keys(CHECKOUT_INFO['phone_number'])

        sleep(FILL_OUT_DELAY)

        # 郵便番号
        locator = MobileMobileCheckoutPageLocator.zip_code
        zip_code = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        zip_code.send_keys(CHECKOUT_INFO['zip_code'])

        sleep(FILL_OUT_DELAY)

        # 都道府県
        locator = MobileMobileCheckoutPageLocator.billing_state
        billing_state = Select(WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator)))
        billing_state.select_by_visible_text(CHECKOUT_INFO['billing_state'])

        sleep(FILL_OUT_DELAY)

        # 区市町村
        locator = MobileMobileCheckoutPageLocator.billing_city
        billing_city = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        billing_city.clear()
        billing_city.send_keys(CHECKOUT_INFO['billing_city'])

        sleep(FILL_OUT_DELAY)

        # 住所
        locator = MobileMobileCheckoutPageLocator.billing_address
        billing_address = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        billing_address.send_keys(CHECKOUT_INFO['billing_address'])

        sleep(FILL_OUT_DELAY)

        # この住所を保存する
        locator = MobileMobileCheckoutPageLocator.store_address_check_box
        store_address_check_box = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        store_address_check_box.click()

        sleep(FILL_OUT_DELAY)

        # 支払い方法
        locator = MobileMobileCheckoutPageLocator.card_type_select_box
        card_type = Select(WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator)))
        card_type.select_by_visible_text(CHECKOUT_INFO['card_type'])

        sleep(FILL_OUT_DELAY)

        # カード番号
        locator = MobileMobileCheckoutPageLocator.card_number
        card_number = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        card_number.send_keys(CHECKOUT_INFO['card_number'])

        sleep(FILL_OUT_DELAY)

        # 有効期限(月) 
        locator = MobileMobileCheckoutPageLocator.card_month_select_box
        card_month_select_box = Select(WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator)))
        card_month_select_box.select_by_value(CHECKOUT_INFO['card_month'])

        sleep(FILL_OUT_DELAY)

        # 有効期限（年）
        locator = MobileMobileCheckoutPageLocator.card_year_select_box
        card_year_select_box = Select(WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator)))
        card_year_select_box.select_by_value(CHECKOUT_INFO['card_year'])

        sleep(FILL_OUT_DELAY)

        # CSV番号
        locator = MobileMobileCheckoutPageLocator.card_cvv
        card_cvv = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        card_cvv.send_keys(CHECKOUT_INFO['card_cvv'])

        sleep(FILL_OUT_DELAY)

        # 利用規約同意
        locator = MobileMobileCheckoutPageLocator.agreement_check_box
        agreement_check_box = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        agreement_check_box.click()

        sleep(FILL_OUT_DELAY)

    def process_payment(self):
        """
        購入する
        """
        locator = MobileCheckoutPageLocator.process_payment
        process_payment = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        process_payment.click()

class MobilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url='https://www.supremenewyork.com/mobile')

    def click_genre(self, genre):
        locator = getattr(MobilePageLocator, genre)
        genre = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        genre.click()

class MobileCategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def click_product(self, product_name):
        locator = MobileCategoryPageLocator.get_product_locator(product_name)
        genre = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        genre.click()

class MobileProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def add_to_cart(self):
        locator = MobileProductPageLocator.add_to_cart_btn
        add_to_cart_btn = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        add_to_cart_btn.click()

    def checkout(self):
        locator = MobileProductPageLocator.checkout_btn
        checkout_btn = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(locator))
        checkout_btn.click()

    def click_product(self, product_name):
        locator = MobileCategoryPageLocator.get_product_locator(product_name)
        genre = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        genre.click()


class MobileCheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def fillout(self):
        """
        お届け先・支払い情報の入力
        """

        # 名前
        locator = MobileCheckoutPageLocator.name
        name = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(locator))
        name.clear()
        name.send_keys(CHECKOUT_INFO['name'])

        sleep(FILL_OUT_DELAY)

        # Eメール
        locator = MobileCheckoutPageLocator.email
        email = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        email.clear()
        email.send_keys(CHECKOUT_INFO['email'])

        sleep(FILL_OUT_DELAY)

        # 電話番号
        locator = MobileCheckoutPageLocator.phone_number
        phone_number = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        phone_number.clear()
        phone_number.send_keys(CHECKOUT_INFO['phone_number'])

        sleep(FILL_OUT_DELAY)

        # 郵便番号
        locator = MobileCheckoutPageLocator.zip_code
        zip_code = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        zip_code.clear()
        zip_code.send_keys(CHECKOUT_INFO['zip_code'])

        sleep(FILL_OUT_DELAY)

        # 都道府県
        locator = MobileCheckoutPageLocator.billing_state
        billing_state = Select(WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator)))
        billing_state.select_by_visible_text(CHECKOUT_INFO['billing_state'])

        sleep(FILL_OUT_DELAY)

        # 区市町村
        locator = MobileCheckoutPageLocator.billing_city
        billing_city = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        billing_city.clear()
        billing_city.send_keys(CHECKOUT_INFO['billing_city'])

        sleep(FILL_OUT_DELAY)

        # 住所
        locator = MobileCheckoutPageLocator.billing_address
        billing_address = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        billing_address.clear()
        billing_address.send_keys(CHECKOUT_INFO['billing_address'])

        sleep(FILL_OUT_DELAY)

        # この住所を保存する
        locator = MobileCheckoutPageLocator.store_address_check_box
        store_address_check_box = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        store_address_check_box.click()

        sleep(FILL_OUT_DELAY)

        # 支払い方法
        locator = MobileCheckoutPageLocator.card_type_select_box
        card_type = Select(WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator)))
        card_type.select_by_visible_text(CHECKOUT_INFO['card_type'])

        sleep(FILL_OUT_DELAY)

        # カード番号
        locator = MobileCheckoutPageLocator.card_number
        card_number = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        card_number.clear()
        card_number.send_keys(CHECKOUT_INFO['card_number'])

        sleep(FILL_OUT_DELAY)

        # 有効期限(月) 
        locator = MobileCheckoutPageLocator.card_month_select_box
        card_month_select_box = Select(WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator)))
        card_month_select_box.select_by_value(CHECKOUT_INFO['card_month'])

        sleep(FILL_OUT_DELAY)

        # 有効期限（年）
        locator = MobileCheckoutPageLocator.card_year_select_box
        card_year_select_box = Select(WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator)))
        card_year_select_box.select_by_value(CHECKOUT_INFO['card_year'])

        sleep(FILL_OUT_DELAY)

        # CSV番号
        locator = MobileCheckoutPageLocator.card_cvv
        card_cvv = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        card_cvv.clear()
        card_cvv.send_keys(CHECKOUT_INFO['card_cvv'])

        sleep(FILL_OUT_DELAY)

        # 利用規約同意
        locator = MobileCheckoutPageLocator.agreement_check_box
        agreement_check_box = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        agreement_check_box.click()

        sleep(FILL_OUT_DELAY)


    def process_payment(self):
        """
        購入する
        """
        locator = MobileCheckoutPageLocator.process_payment
        process_payment = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
        process_payment.click()