import time
import logging
from selenium.webdriver.common.by import By
from config import GA_EMAIL, GA_SENHA

URL_LOGIN_GA = "https://ga.flashcourier.com.br/"

logging.basicConfig(level=logging.INFO)

def realizar_login_ga(driver, pagina):

    driver.get(URL_LOGIN_GA + f"{pagina}")
    
    time.sleep(4)
    
    usuario_box = driver.find_element(By.NAME, "email")
    senha_box = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, '//*[@id="login"]/section/form/div[3]/button')

    usuario_box.send_keys(GA_EMAIL)
    senha_box.send_keys(GA_SENHA)
    login_button.click()
    
    logging.info("Login realizado com sucesso.")

    time.sleep(5)