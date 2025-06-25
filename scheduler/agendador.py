import schedule
import time
from scheduler.agenda import configurar_agendamentos

def iniciar_agendador():
    print(">>> Iniciando configuração de agendamentos...")
    configurar_agendamentos()
    print("⏰ Agendador iniciado.")
    while True:
        schedule.run_pending()
        time.sleep(1)