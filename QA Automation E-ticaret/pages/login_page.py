from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID,"user-name")
    PASSWORD = (By.ID,"password")
    BUTTON = (By.XPATH,"//input[@type='submit']")

    def __init__(self,driver):
        super().__init__(driver)
       
    
    def enter_username(self,username):
        self.type(self.USERNAME,username)
    
    def enter_password(self,password):
        self.type(self.PASSWORD,password)
    
    def click_button(self):
        self.click(self.BUTTON)     
