from config import GA_EMAIL, GA_SENHA, SAFRA_SHORTNAME, SAFRA_USUARIO, SAFRA_SENHA, EMAIL_DESTINO, NOME_PLANILHA_ORIGINAL, CLIENTES_DIR, BASE_DIR
from src.email.disparador_email import enviar_email
from rpa.driver_safra import configurar_driver_safra
from rpa.driver import configurar_driver
from rpa.extrator_arquivo_safra import navegar_para_retorno
from rpa.extrator_arquivo_safra import fazer_download_arquivo_safra
from rpa.autenticadores.login_safra import realizar_login_safra
from rpa.autenticadores.login_ga import realizar_login_ga
from utils.gerenciador_arquivos import capturar_arquivos_envio_safra
from utils.formatter import formatar_corpo_html_safra
from rpa.enviar_arquivo_ga import enviar_arquivo_ga

def executar(): 
    try:
        
        print("\n🟢 Iniciando processamento: SAFRA")

        cliente = "safra"
        backup_dir = CLIENTES_DIR[cliente]["backup"]
        
        driver_safra = configurar_driver_safra()
        driver_ga = configurar_driver(headless=False)
        
        #Realiza o login no site safra
        realizar_login_safra(driver_safra, SAFRA_SHORTNAME, SAFRA_USUARIO, SAFRA_SENHA)
        
        
        #Faz o processo de extração do arquivo
        navegar_para_retorno(driver_safra)
        data, hora = fazer_download_arquivo_safra(driver_safra)

        #Realiza a extração da nomenclatura dos arquivos a serem enviados
        nomenclatura_arquivos = capturar_arquivos_envio_safra(BASE_DIR)
        
        
        #Realiza o Login no ga
        realizar_login_ga(driver_ga, "processamentos/upload")
        

        #Realiza o envio do arquivo ao ga
        enviar_arquivo_ga(driver_ga, nomenclatura_arquivos, backup_dir, "BANCO_SAFRA_SAOBSAF02_REM")
        

        #realiza o envio do e-mail
        enviar_email(
        assunto="✅ RPA SAFRA - Execução Concluída com Sucesso.",
        corpo=formatar_corpo_html_safra(data, hora, sucesso=True),
        destinatarios=EMAIL_DESTINO
    )

    except Exception as e:
        enviar_email(
            assunto="❌ RPA SAFRA - Erro na Execução",
            corpo=formatar_corpo_html_safra(erro=str(e), sucesso=False),
            destinatarios=EMAIL_DESTINO
        )
        print(f"Ocorreu um erro: {e}")
    
    finally:
        driver_safra.quit
        driver_ga.quit()
    
    print(f"✅ Processamento finalizado: {cliente.upper()}")