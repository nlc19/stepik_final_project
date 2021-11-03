from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_promo_param_in_link(self):
        assert ProductPageLocators.PROMO_PARAM_IN_LINK in self.browser.current_url, "Link doesn't contain promo " \
                                                                                    "parameter"

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is " \
                                                                                   "not presented"
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_addition_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Successful addition message is " \
                                                                              "not present"
        selected_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text == selected_product_name, \
            "The added product does not match the selected product"

    def should_be_correct_total_cost(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_COST_IN_BASKET_MESSAGE), "Total cost in basket " \
                                                                                           "message is not present"
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.TOTAL_COST_IN_BASKET).text == price, "Total cost " \
            "in basket does not match the price of the selected product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, " \
                                                                                  "but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should have disappeared"
