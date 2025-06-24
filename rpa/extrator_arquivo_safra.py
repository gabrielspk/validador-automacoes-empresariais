from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def navegar_para_retorno(driver):
    consulta_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="menu-principal-1"]/a'))
    )
    consulta_button.click()

    print("Navegado para consulta")

    time.sleep(5)

    retorno_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="body"]/main/conteudo-pagina/div[2]/div/div[2]/div/div[1]/div/div/div/ul/li[2]'))
    )
    retorno_button.click()

    print("navegado para retorno")

    time.sleep(4)

def fazer_download_arquivo_safra(driver):
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "tbody"))
    )
    
    linhas = tabela.find_elements(By.TAG_NAME, "tr")  #Encontra todas as linhas dentro do <tbody>
    
    #laço para percorrer "tr" e seus respectivos "td"
    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")
        if colunas:
            print(f"Download iniciado do arquivo de quantidade de linhas: {colunas[1].text}")
            data_arquivo = colunas[1].text
            link_download = linha.find_element(By.CSS_SELECTOR, "a[ng-click='ctrl.download(item)']")
            link_download.click()
            time.sleep(5)
            break

    return data_arquivo