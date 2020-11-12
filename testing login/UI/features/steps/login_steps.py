from antioch_ui import utils
from behave import given, when, then
import time

from features.pages.login_page import LoginPage
from features.pages.home_page import HomePage
from features.pages.sign_up_page import SignUp

# Givens


@given('I want to log in to Hudl as {}')
def go_to_login_page(context, user):
    context.user = utils.load_user_json(context, user)
    context.browser.load(context, '')

@given('I want to create new account on Hudl as {}')
def go_to_login_page(context, user):
    context.user = utils.load_user_json(context, user)
    context.browser.load(context, '')
    time.sleep(5)
    

# Whens

@when('I log in')
def doLogin(context):
   
    login_page = LoginPage(context.browser)
    login_page.enter_email(context.user['user'])
    login_page.enter_password(context.password)
    login_page.click_login_button()
    





@when('I force log in')
def doForceLogin(context):
    """
    :param context: Behave context object
    Simple login with the context user and password
    """
    login_page = LoginPage(context.browser)
    login_page.enter_email(context.user['user'])
    login_page.enter_password(context.password)
    login_page.click_login_button()
    login_page.click_force_login_button()


@when('I click on Home Button')
def click_home_page(context):
    home_page = HomePage(context.browser)
    home_page.click_home_page()
    time.sleep(5)    

@when('I click on sign up button')
def click_sign_up_button(context):
    login_page = LoginPage(context.browser)
    login_page.click_sign_up_button()
    time.sleep(5)    





# Thens

@then('I should be directed to my home page')
def check_landed_on_profile_page(context):
    home_page = HomePage(context.browser)
    assert home_page.is_page_loaded(), 'User not directed to home page after login'



@then('I should be directed to my sign up page')
def is_sign_up_page_visible(context):
    sign_up_page = SignUp(context.browser)
    assert sign_up_page.is_page_loaded(), 'User not directed to sign up page  after clicking on sign up button'
    time.sleep(10)

    
