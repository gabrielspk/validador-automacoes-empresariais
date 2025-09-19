from config import GA_EMAIL, GA_SENHA, EMAIL_DESTINO_NUCELL, NOME_PLANILHA_ORIGINAL, CLIENTES_DIR, SAIDA_PATH, BASE_DIR
from rpa.driver import configurar_driver
from rpa.extrator_planilha_ga import baixar_planilha
from rpa.autenticadores.login_ga import realizar_login_ga
from src.carregamento.leitor_planilha import carregar_dados
from src.mercado_pago.gerador import gerar_relatorio, salvar_relatorio_com_validacao
from src.mercado_pago.validador import validar_registros
from utils.formatter import formatar_corpo_html_anexo
from utils.base_relatorio import gerar_tabela_html
from src.email.disparador_email import enviar_email
from utils.gerenciador_arquivos import mover_e_renomear_planilha, mover_para_backup
from utils.anexo_email import capturar_anexo_email
import datetime

def executar():
    
    print("\n🟢 Iniciando processamento: NUCELL")

    cliente = "nubank"

    #Declara datas do dia atual e dia anterior
    data_atual = datetime.date.today()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y")
    data_anterior = data_atual - datetime.timedelta(days=1)
    data_anterior_formatada = data_anterior.strftime("%d/%m/%Y")


    #Faz o processo de RPA
    driver = configurar_driver(headless=False)
    realizar_login_ga(driver, "logs")
    baixar_planilha(driver, "nucell")
    driver.quit() 

    #Declara os caminhos
    origem = BASE_DIR / NOME_PLANILHA_ORIGINAL
    entrada_dir = CLIENTES_DIR[cliente]["entrada"]
    backup_dir = CLIENTES_DIR[cliente]["backup"]

    #captura planilha baixada
    anexo_planilha = capturar_anexo_email(caminho_arquivo=BASE_DIR, nome_arquivo=NOME_PLANILHA_ORIGINAL, tipo="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    #move a planilha
    entrada_path, backup_path = mover_e_renomear_planilha(cliente, origem, entrada_dir, backup_dir)

    #Formatação e envio por e-mail
    corpo_email = formatar_corpo_html_anexo(cliente=cliente)
    assunto = (f"✅ Processamento Nubank - NUCELL {data_anterior_formatada} a {data_atual_formatada}"
    )
    enviar_email(assunto=assunto, corpo=corpo_email, destinatarios=EMAIL_DESTINO_NUCELL, anexos=[anexo_planilha])

    #Move para backup
    mover_para_backup(entrada_path, backup_path)

    print(f"✅ Processamento finalizado: {cliente.upper()}")