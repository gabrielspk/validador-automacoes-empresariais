from scheduler.agendador import iniciar_agendador
from app import mercado_pago, redecard, skypostal, safra, itau

def main():

    #mercado_pago.executar()
    #redecard.executar()
    #skypostal.executar()
    #safra.executar()
    #itau.executar()
    
    iniciar_agendador()
    
if __name__ == "__main__":
    main()