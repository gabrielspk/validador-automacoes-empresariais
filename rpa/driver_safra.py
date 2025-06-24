from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import BASE_DIR

def configurar_driver_safra():
    options = Options()
    options.add_argument("--start-maximized")  # Abre maximizado
    options.add_argument("--disable-gpu")  # Desativa GPU (corrige alguns erros gráficos)
    options.add_argument("--disable-software-rasterizer")  # Renderização em software
    options.add_argument("--incognito")  # Abre o chrome em modo anônimo
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remove a mensagem que o chrome está sendo controlado por automação
    options.add_experimental_option("useAutomationExtension", False)  # Desativa a extensão de automação do chrome
    options.add_argument("--ignore-certificate-errors")  # Ignora erros de certificado SSL
    options.add_argument("--disable-web-security")  # Desativa a política de segurança do navegador
    options.add_argument("--allow-insecure-localhost")  # Permite acesso a sites inseguros hospedados localmente

    prefs = {
        "download.default_directory": r"c:\Users\gabriel.ferreira\Downloads",  # Diretório de download
        "download.prompt_for_download": False,  # Desativa caixa de diálogo de download
        "download.directory_upgrade": True,  # Permite atualizações no diretório
        "safebrowsing.enabled": True,  # Ativa navegação segura
        "profile.default_content_settings.popups": 0,  # Bloqueia popups
        "download.extensions_to_open": "txt",  # Não abre extensões automaticamente
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,  # Permite múltiplos downloads
        "profile.default_content_settings.cookies": 2,
        "download.open_pdf_in_system_reader": False,  # Não abre PDFs automaticamente
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })
    return driver