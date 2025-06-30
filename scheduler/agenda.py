"""
Configuração dos horários de validação para cada cliente.
Formato: { cliente: [ 'HH:MM', ... ] }
"""

VALIDACAO_HORARIOS = {
    "mercado_pago": ["09:45"],
    "redecard": ["10:30"],
    "skypostal": ["10:00"],
    "safra": ["09:00"],
    "itau": ["09:00"]
}

from scheduler.tarefas import MAPA_TAREFAS
import schedule

def configurar_agendamentos():
    for cliente, horarios in VALIDACAO_HORARIOS.items():
        tarefa = MAPA_TAREFAS.get(cliente)
        if tarefa:
            for horario in horarios:
                schedule.every().day.at(horario).do(tarefa)
                print(f"🔁 Criando agendamento para {cliente} às {horario} | id da função: {id(tarefa)}")
        else:
            print(f"⚠️ Nenhuma tarefa definida para: {cliente}")