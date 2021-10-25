from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login link is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER), "Login email field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_LINK), 'Link "I\'ve forgotten my password" ' \
                                                                                 'is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Register email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), "Register password field for registration" \
                                                                         " is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_CONFIRM_PASSWORD), "Register Confirm password field is " \
                                                                                 "not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Register button is not presented"
