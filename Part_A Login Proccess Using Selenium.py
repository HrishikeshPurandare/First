from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName = "chrome" #Here chrome or firefiz any browser can be used


if browserName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())

elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
   print('please pass the correct browser name :' + browserName)
   raise Exception('driver is not found')

driver.implicitly_wait(15)
driver.maximize_window()
driver.get("https://www.hudl.com") #login to hudl using correct credentials

feature_link = driver.find_element(By.LINK_TEXT, 'Log in').click()
time.sleep(10)

driver.find_element(By.ID, 'email').send_keys("hmpurandare44@gmail.com")
driver.find_element(By.ID, 'password').send_keys("****")

driver.find_element(By.ID, 'logIn').click()
time.sleep(20)
driver.find_element_by_xpath("//body[@class='mobile-first']/div[@id='ssr-webnav']/div[@class='hui-webnav hui-webnav-mobile__you hui-webnav--menu-closed']/div[@class='hui-webnav__grid hui-navcontainer']/nav[@class='hui-webnav__grid-col--onewhole hui-primarynav uni-environment--dark uni-env--dark']/div[@class='hui-primaryteamswitcher hui-primaryteamswitcher--has-teams']/a[@class='hui-primaryteamswitcher__item hui-primaryteamswitcher__item--team hui-primaryteamswitcher__item--selected']/div[2]").click()
driver.find_element_by_xpath("//span[contains(text(),'QA Hire Project')]").click()  #it will navigate to Coach's acoount
time.sleep(30)
#After that logged out from account
driver.find_element_by_xpath("//div[@class='hui-globaluseritem__display-name']//span[contains(text(),'Hrishikesh Purandare')]").click()
driver.find_element_by_xpath("//div[@class='hui-globaladditionalitems hui-globaladditionalitems--not-phone']//a[@class='hui-globalusermenu__item']").click()
print(driver.title)
time.sleep(15)
driver.quit()
print("login successfull")
