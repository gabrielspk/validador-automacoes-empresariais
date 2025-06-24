from config import GA_EMAIL, GA_SENHA, EMAIL_DESTINO, NOME_PLANILHA_ORIGINAL, CLIENTES_DIR, SAIDA_PATH, BASE_DIR
from rpa.driver import configurar_driver
from rpa.extrator_planilha_ga import baixar_planilha
from rpa.autenticadores.login_ga import realizar_login_ga
from src.carregamento.leitor_planilha import carregar_dados
from src.redecard.gerador import gerar_relatorio, salvar_relatorio_com_validacao
from src.redecard.validador import validar_registros
from utils.formatter import formatar_corpo_html
from utils.base_relatorio import gerar_tabela_html
from src.email.disparador_email import enviar_email
from utils.gerenciador_arquivos import mover_e_renomear_planilha, mover_para_backup
import datetime

def executar():
    
    print("\n🟢 Iniciando processamento: REDECARD")

    cliente = "redecard"

    #Declara datas do dia atual e dia anterior
    data_atual = datetime.date.today()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y")
    data_anterior = data_atual - datetime.timedelta(days=1)
    data_anterior_formatada = data_anterior.strftime("%d/%m/%Y")


    #Faz o processo de RPA    
    driver = configurar_driver(headless=True)
    realizar_login_ga(driver, "logs")
    baixar_planilha(driver, "redecard")
    driver.quit()


    #Declara os caminhos
    origem = BASE_DIR / NOME_PLANILHA_ORIGINAL
    entrada_dir = CLIENTES_DIR[cliente]["entrada"]
    backup_dir = CLIENTES_DIR[cliente]["backup"]

    #Move a planilha
    entrada_path, backup_path = mover_e_renomear_planilha(cliente, origem, entrada_dir, backup_dir)


    #Faz a validação
    df = carregar_dados(entrada_path)
    if df is None:
        print("❌ Nenhum dado carregado para Redecard.")
        return

    relatorio = gerar_relatorio(df)
    salvar_relatorio_com_validacao(relatorio, SAIDA_PATH)
    divergencias = validar_registros(relatorio)


    #Formatação e envio por e-mail
    corpo_tabela = gerar_tabela_html(relatorio)
    corpo_email = formatar_corpo_html(corpo_tabela, divergencias)
    assunto = (
        f"⚠️ VALIDAÇÃO REDECARD {data_anterior_formatada} e {data_atual_formatada} - VERIFICAR DIVERGÊNCIAS ENCONTRADAS"
        if divergencias else
        f"✅ VALIDAÇÃO REDECARD {data_anterior_formatada} e {data_atual_formatada} - VALIDADO COM SUCESSO"
    )
    enviar_email(assunto=assunto, corpo=corpo_email, destinatarios=EMAIL_DESTINO)


    #Move para backup
    mover_para_backup(entrada_path, backup_path)

    print(f"✅ Processamento finalizado: {cliente.upper()}")