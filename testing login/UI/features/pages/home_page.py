from antioch_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """
    Wyscout Home Page
    """

    HOME_PAGE = (By.CSS_SELECTOR, '.uni-form__input')
    HOME_BUTTON = (By.CSS_SELECTOR, '.hui-globalnav__home > span')
   

    
    def is_page_loaded(self):
        return self.browser.wait.until_element_visible(*self.HOME_PAGE)

    def click_home_page(self):
        return self.browser.wait.until_element_visible(*self.HOME_BUTTON).click() 
    
 

  



        

    
            