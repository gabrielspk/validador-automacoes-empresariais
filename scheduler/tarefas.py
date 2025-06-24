from app import mercado_pago, redecard, skypostal, safra

def tarefa_mercado_pago():
    mercado_pago.executar()

def tarefa_redecard():
    redecard.executar()

def tarefa_skypostal():
    skypostal.executar()

def tarefa_safra():
    safra.executar()

MAPA_TAREFAS = {
    "mercado_pago": tarefa_mercado_pago,
    "redecard": tarefa_redecard,
    "skypostal": tarefa_skypostal,
    "safra": tarefa_safra
}