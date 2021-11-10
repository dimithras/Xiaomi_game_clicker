from selenium import webdriver

from selenium.common.exceptions import ElementClickInterceptedException as Non_Clicable
from selenium.common.exceptions import TimeoutException as Time_Out
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from random import uniform as rand
from random import randint
import time

def register(time, driver):
    return WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.register')))
def get_Forward(time, driver):
    return WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.slider_button.forward')))
def get_Green(time, driver):
    return WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.trigger.green')))
def get_Rate(driver):
    return driver.find_element_by_xpath('/html/body/app-root/games/div/div/div[1]/div/div[2]/div[2]/div[2]').get_attribute('innerHTML').strip()
def click_Num(driver):
    number_of_clicks = ''
    for e in driver.find_elements_by_css_selector('.digit'):
        number_of_clicks+=e.get_attribute('innerHTML').strip()
    return int(number_of_clicks)
    
driver_path = r"C:\WebDriver\bin\Brave_chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
profile_path = r""
option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument(profil_path) 
# option.add_argument("--headless")

browser = webdriver.Chrome(executable_path=driver_path, options=option)

browser.get("https://cinemagicgame.igm.gg/")

try:
    register(10,browser)
except Time_Out:
    pass

get_Forward(300, browser)

rate = ''
clicks = 0
try:
    while clicks < 999999:
        time.sleep(randint(0,5))
        forward = get_Forward(50, browser)
        while forward:
            time.sleep(rand(0, 3))
            forward.click()
            try:
                forward = get_Forward(1, browser)
            except Time_Out:
                forward = False
                pass
        if rate != get_Rate(browser):
            rate = get_Rate(browser)
            print("Rating: " + rate)
        try:
            while True:
                get_Green(10, browser).click
        except Non_Clicable:
            pass
        except Time_Out:
            pass
        if click_Num(browser) == 999999:
            print("Seems like we've reached maximum number")
            break
        clicks = click_Num(browser)
        print(clicks)
except KeyboardInterrupt:
    print("Program interrupted")
    
get_Forward(500, browser)
browser.quit()
