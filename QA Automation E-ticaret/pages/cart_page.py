from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    #CART_PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_TITLE =  (By.CLASS_NAME, "title")
    def __init__(self, driver):
        super().__init__(driver)
    #def get_product_name(self):
     #return self.get_text(self.CART_PRODUCT_NAME)  
    def go_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON) 
    def get_cart_title(self):
        return self.get_text(self.CART_TITLE)     

        