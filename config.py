import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

GA_EMAIL = os.getenv("GA_EMAIL")
GA_SENHA = os.getenv("GA_SENHA")

SAFRA_SHORTNAME = os.getenv("SAFRA_SHORTNAME")
SAFRA_USUARIO = os.getenv("SAFRA_USUARIO")
SAFRA_SENHA = os.getenv("SAFRA_SENHA")

HOST_SMTP = os.getenv("HOST_SMTP")
MAILGRID_USUARIO = os.getenv("MAILGRID_USUARIO")
MAILGRID_SENHA = os.getenv("MAILGRID_SENHA")


EMAIL_DESTINO = os.getenv("EMAIL_DESTINO").split(",")
EMAIL_DESTINO_PESSOAL = os.getenv("EMAIL_DESTINO_PESSOAL").split(",")

BASE_DIR = Path(r"C:\Users\gabriel.ferreira\Downloads")

NOME_PLANILHA_ORIGINAL = "Arquivos Processados.xlsx"

CLIENTES_DIR = {
    "mercado_pago": {
        "entrada": BASE_DIR / "mercado_pago" / "entrada",
        "backup": BASE_DIR / "mercado_pago" / "backup"
    },
    "redecard": {
        "entrada": BASE_DIR / "redecard" / "entrada",
        "backup": BASE_DIR / "redecard" / "backup"
    },
    "skypostal": {
        "entrada": BASE_DIR / "skypostal" / "entrada",
        "backup": BASE_DIR / "skypostal" / "backup"
    },
    "safra": {
        "backup": BASE_DIR / "safra" / "backup"
    },
    "itau": {
        "entrada": BASE_DIR / "itau" / "entrada",
        "backup": BASE_DIR / "itau" / "backup"
    },
    "nubank": {
        "entrada": BASE_DIR / "nubank" / "entrada",
        "backup": BASE_DIR / "nubank" / "backup"
    }
}

SAIDA_PATH = BASE_DIR / "RelatorioValidacao.xlsx"