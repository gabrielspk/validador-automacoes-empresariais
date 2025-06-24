import pandas as pd

def carregar_dados(caminho):
    try:
        return pd.read_excel(caminho)
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None