from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver= driver
        self.wait = WebDriverWait(driver,10)
    def find(self, locator):
        return self.wait.until(
        EC.element_to_be_clickable(locator)
    )
    def click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)
    def type(self,locator,text):
        self.find(locator).send_keys(text)  


    def get_title(self):
            return self.driver.title

    def get_current_url(self):
         return self.driver.current_url
    def get_text(self,locator):
         return self.find(locator).text
                   