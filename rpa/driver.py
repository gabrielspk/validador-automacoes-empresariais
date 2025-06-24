from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def configurar_driver(headless=True):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")  # evita problemas gráficos
        options.add_argument("--window-size=1920,1080")  # necessário em headless    
    
    driver = webdriver.Chrome(options=options)
    return driver