from antioch_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

from features.pages.login_page import LoginPage
from features.pages.home_page import HomePage



class SignUp(BasePage):
    """
    Sign UP Page
    """

    SIGN_UP_PAGE = (By.ID, 'FirstName')
    
   

    
    def is_page_loaded(self):
        return self.browser.wait.until_element_visible(*self.SIGN_UP_PAGE)
    