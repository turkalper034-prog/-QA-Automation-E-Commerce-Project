from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class InventoryPage(BasePage):
    PRODUCTS_TİTLE = (By.XPATH,"//span[@class='title']")
    BİKE_LİGHT_BUTTON = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self,driver):
        super().__init__(driver)

    def get_products_title(self):
        return self.get_text(self.PRODUCTS_TİTLE)   
    def add_bike_light_button(self):
        self.click(self.BİKE_LİGHT_BUTTON)
    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)    
    def go_to_cart(self):
        self.click(self.CART_LINK)
