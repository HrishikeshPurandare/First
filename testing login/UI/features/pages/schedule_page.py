from antioch_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

from features.pages.login_page import LoginPage
from features.pages.home_page import HomePage



class SchedulePage(BasePage):
    """
    Teams Schedule Page
    """

    SCHEDULE_PAGE = (By.ID, 'season-label-container')
    TEAM_BUTTON = (By.CSS_SELECTOR, '.hui-primarynav__item--dropdown')
    SCHEDULE_TAB = (By.CSS_SELECTOR, '.hui-primarysubnav__item:nth-child(3) > span')
   

    
    def is_page_loaded(self):
        return self.browser.wait.until_element_visible(*self.SCHEDULE_PAGE)

    def click_team_button(self):
        return self.browser.wait.until_element_visible(*self.TEAM_BUTTON).click()

    def click_schedule_tab(self):
        return self.browser.wait.until_element_visible(*self.SCHEDULE_TAB).click()      