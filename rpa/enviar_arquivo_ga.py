import time
import shutil
from selenium.webdriver.common.by import By

def enviar_arquivo_ga(driver, nomenclatura_arquivos, backup_dir, nome_processo_ga):
    processo_box = driver.find_element(By.NAME, "nome-processo")
    processo_box.send_keys(nome_processo_ga)
    print("enviado nome do processo")

    time.sleep(4)

    arquivo_box = driver.find_element(By.NAME, "arquivo[]")
    for arquivo in nomenclatura_arquivos:
            print(f"Carregando arquivo {arquivo}")
            arquivo_box.send_keys(arquivo)
            time.sleep(2)

    enviar_arquivo_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/form/div[3]/div/div/div/div/div[2]/button")
    enviar_arquivo_button.click()

    time.sleep(2)

    print(f"Movendo arquivos: {nomenclatura_arquivos} para backup.")

    shutil.move(arquivo, backup_dir)
    
    time.sleep(100)