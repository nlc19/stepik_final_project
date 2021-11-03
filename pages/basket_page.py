from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "There is product item in the " \
                                                                                   "empty basket, but should not be"

    def should_be_message_in_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "The text that the basket is empty is " \
                                                                          "not presented"
