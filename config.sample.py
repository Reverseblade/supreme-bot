CHROME_DRIVER_PATH = '' #chromedriverのフルパス
MULTI_PROCESS_COUNT = 2
PROXY = None
ADD_TO_CART_DELARY = 5
FILL_OUT_DELAY = 0
AUTO_PROCESS_PAYMENT = False
PRODUCT_LIST = [
        {
                'id': 1,
                'href': '/shop/jackets/x4x6e5lns/u9qk3m1df',
                'size': 'Medium'
        },
        {
                'id': 2,
                'href': '/shop/tops-sweaters/tb5rx4l6y/kxwj7nipz',
                'size': 'Large'
        },
        {
                'id': 3,
                'href': '/shop/accessories/sju50wchy/a30rfwy2l',
                'size': None
        },
]
CHECKOUT_INFO = {
            'name': '山田 太郎',
            'email': 'aaa@bb.cc',
            'phone_number': '12345678910',
            'zip_code': '1234567',
            'billing_state': '東京都',
            'billing_city': '港区六本木',
            'billing_address': '1-2-3',
            'card_type': 'Mastercard',
            'card_number': '1111222233334444',
            'card_month': '01',
            'card_year': '2025',
            'card_cvv': '123'
        }