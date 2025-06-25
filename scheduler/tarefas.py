from app import mercado_pago, redecard, skypostal, safra, itau

def tarefa_mercado_pago():
    mercado_pago.executar()

def tarefa_redecard():
    redecard.executar()

def tarefa_skypostal():
    skypostal.executar()

def tarefa_safra():
    safra.executar()

def tarefa_itau():
    itau.executar()

MAPA_TAREFAS = {
    "mercado_pago": tarefa_mercado_pago,
    "redecard": tarefa_redecard,
    "skypostal": tarefa_skypostal,
    "safra": tarefa_safra,
    "itau":  tarefa_itau
}