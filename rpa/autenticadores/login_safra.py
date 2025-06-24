from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.blocking import BlockingScheduler
import time

URL_LOGIN_SAFRA = "http://www.lignetsafra.net.br/ibj.html#/"

def realizar_login_safra(driver, shortname, username, password):
    driver.get(URL_LOGIN_SAFRA)  #Acessa o site

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-model="ctrl.shortname"]'))
    ).send_keys(shortname)
    

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-model="ctrl.username"]'))
    ).send_keys(username)

    time.sleep(1)

    login_button = driver.find_element(By.XPATH, '//*[@id="body"]/main/div[2]/div[2]/login-component/section/div[2]/form/div[3]/button')
    login_button.click()

    time.sleep(3)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[ng-model="Ctrl.pass"]'))
    ).send_keys(password)

    continue_button = driver.find_element(By.XPATH, '//*[@id="body"]/main/div[2]/div[2]/section/div[2]/form/div[3]/button')
    continue_button.click()

    time.sleep(10)