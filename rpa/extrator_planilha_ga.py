import time
import logging
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)

def baixar_planilha(driver, filtro_pesquisa, dias_pesquisa=1):
    
    data_input = driver.find_element(By.ID, "data-inicio")
    
    data_atual = data_input.get_attribute("value")
    data_obj = datetime.strptime(data_atual, "%d/%m/%Y")

    if dias_pesquisa is not None:
        nova_data = data_obj - timedelta(days=dias_pesquisa)
        data_formatada = nova_data.strftime("%d/%m/%Y")
        
        data_input.clear()
        data_input.send_keys(data_formatada)
        time.sleep(2)

    # Aplica o filtro
    driver.find_element(By.XPATH, '//*[@id="dataTableBuilder_filter"]/label/input').send_keys(filtro_pesquisa)
    time.sleep(1)

    # Baixa a planilha
    download_button = driver.find_element(By.XPATH, '//*[@id="spreadsheet"]')
    download_button.click()

    logging.info(f"Download solicitado para data de {dias_pesquisa} dia(s) atrás.")
    time.sleep(30)