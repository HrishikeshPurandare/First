from antioch_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """
    Hudl Login Page
    """

    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#logIn")
    SIGN_UP_BUTTON = (By.LINK_TEXT,'Sign up')
        #FORCE_LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn2_zFM")
    

    def enter_email(self, email):
        element = self.browser.wait.until_element_visible(*self.EMAIL_FIELD)
        element.click()
        element.send_keys(email)

    def enter_password(self, password):
        self.browser.wait.until_element_clickable(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.browser.wait.until_element_clickable(*self.LOGIN_BUTTON).click()  

    def click_sign_up_button(self):
        self.browser.wait.until_element_clickable(*self.SIGN_UP_BUTTON).click()     

     


