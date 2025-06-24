import time
import logging
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)

def baixar_planilha(driver, filtro_pesquisa):
    
    data_input = driver.find_element(By.ID, "data-inicio")
    
    data_atual = data_input.get_attribute("value")
    data_obj = datetime.strptime(data_atual, "%d/%m/%Y")

    data_anterior = data_obj - timedelta(days=1)
    data_formatada = data_anterior.strftime("%d/%m/%Y")

    data_input.clear()
    data_input.send_keys(data_formatada)

    time.sleep(2)
    
    driver.find_element(By.XPATH, '//*[@id="dataTableBuilder_filter"]/label/input').send_keys(filtro_pesquisa)
    time.sleep(1)

    download_button = driver.find_element(By.XPATH, '//*[@id="spreadsheet"]')
    download_button.click()

    logging.info("Download da planilha solicitado.")
    time.sleep(30)