# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ShopPageLocator:

    def __init__(self):
        pass

    shop_all = (By.XPATH, '//*[@id="nav-store"]/li[1]/a')
    
class ShopAllPageLocator:

    def __init__(self):
        pass

    target_product = (By.XPATH, '//a[@href="/shop/jackets/x4x6e5lns/u9qk3m1df"]')

class ProductPageLocator:

    def __init__(self):
        pass

    size_select_box = (By.XPATH, '//*[@id="size"]') 
    add_btn = (By.NAME, 'commit')
    checkout_btn = (By.XPATH, '//*[@id="cart"]/a[2]')
    shop_all = (By.XPATH, '//*[@id="nav-store"]/li[1]/a')


class CheckoutPageLocator:
    def __init__(self):
        pass

    name = (By.XPATH, '//*[@id="order_billing_name"]')
    email = (By.XPATH, '//*[@id="order_email"]')
    phone_number = (By.XPATH, '//*[@id="order_tel"]')
    zip_code = (By.XPATH, '//*[@id="order_billing_zip"]')
    billing_state = (By.XPATH, '//*[@id="order_billing_state"]')
    billing_city = (By.XPATH, '//*[@id="order_billing_city"]')
    billing_address = (By.XPATH, '//*[@id="order_billing_address"]')
    store_address_check_box = (By.XPATH, '//*[@id="cart-address"]/fieldset/div[8]/div/ins')
    card_type_select_box = (By.XPATH, '//*[@id="credit_card_type"]')
    card_number = (By.XPATH, '//*[@id="cnb"]')
    card_cvv = (By.XPATH, '//*[@id="vval"]')
    card_month_select_box = (By.XPATH, '//*[@id="credit_card_month"]')
    card_year_select_box = (By.XPATH, '//*[@id="credit_card_year"]')
    agreement_check_box = (By.XPATH, '//*[@id="order_terms"]')
    process_payment = (By.XPATH, '//*[@id="pay"]/input')
