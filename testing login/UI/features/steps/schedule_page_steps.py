from antioch_ui import utils
from behave import given, when, then
import time


from features.pages.home_page import HomePage
from features.pages.schedule_page import SchedulePage



# Whens

@when('I click on team button')
def click_team_button(context):
    schedule_page = SchedulePage(context.browser)
    schedule_page.click_team_button()
    time.sleep(5)    

@when('I click on Schedule Button')
def click_schedule_tab(context):
    schedule_page = SchedulePage(context.browser)
    schedule_page.click_schedule_tab()
    time.sleep(5)    
# Thens

@then('I should be directed to my schedule page')
def check_landed_on_profile_page(context):
    schedule_page = SchedulePage(context.browser)
    assert schedule_page.is_page_loaded(), 'User not directed to home page after login'

    
