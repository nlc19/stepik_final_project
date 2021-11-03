from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "span > a.btn")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_PARAM_IN_LINK = 'login'
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    LOGIN_USER = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "#login_form a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')

    REG_FORM = (By.CSS_SELECTOR, ".register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    PROMO_PARAM_IN_LINK = "?promo="
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-safe:nth-child(1) .alertinner')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert.alert-safe:nth-child(1) strong')
    TOTAL_COST_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-safe:nth-child(3) .alertinner')
    TOTAL_COST_IN_BASKET = (By.CSS_SELECTOR, '.alert:nth-child(3) strong')


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .basket-items")