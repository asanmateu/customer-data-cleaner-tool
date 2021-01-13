from constants import CUSTOMER_CODE, CUSTOMER_NAME, ADDRESS_CODE, ADDRESS_1, ADDRESS_2, CITY, ZIP, PHONE, \
    BUYER_NAME, EMAIL, PRICE_CURRENCY, DISCOUNT, STORE_NAME, STATE


# Character limits for validation fields...
LIMITS = {
    CUSTOMER_CODE: 100,
    CUSTOMER_NAME: 150,
    ADDRESS_CODE: 100,
    STORE_NAME: 255,
    ADDRESS_1: 100,
    ADDRESS_2: 100,
    CITY: 150,
    STATE: 40,
    ZIP: 20,
    PHONE: 30,
    BUYER_NAME: 200,
    EMAIL: 200,
    PRICE_CURRENCY: 3,
    DISCOUNT: 3,
}