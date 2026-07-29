from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CHECKOUT_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID,"finish")

    def __init__(self, driver):
        super().__init__(driver)

    def get_checkout_title(self):
        return self.get_text(self.CHECKOUT_TITLE)

    def enter_first_name(self, first_name):
        self.type(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.type(self.LAST_NAME, last_name)

    def enter_postal_code(self, postal_code):
        self.type(self.POSTAL_CODE, postal_code)

    def get_first_name_value(self):
        return self.find(self.FIRST_NAME).get_attribute("value")

    def get_last_name_value(self):
        return self.find(self.LAST_NAME).get_attribute("value")

    def get_postal_code_value(self):
        return self.find(self.POSTAL_CODE).get_attribute("value")

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
    def click_finish_button(self):
        self.click(self.FINISH_BUTTON)    