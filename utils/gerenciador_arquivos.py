import shutil
from datetime import datetime
from pathlib import Path
import os

def mover_e_renomear_planilha(cliente: str, origem: Path, entrada_dir: Path, backup_dir: Path):
    
    hoje = datetime.today().strftime("%Y-%m-%d")
    nome_base = f"{cliente.lower().replace(' ', '_')}_{hoje}.xlsx"
    destino_entrada = entrada_dir / nome_base

    entrada_dir.mkdir(parents=True, exist_ok=True)
    backup_dir.mkdir(parents=True, exist_ok=True)

    if destino_entrada.exists():
        contador = 1
        while True:
            novo_nome = destino_entrada.with_stem(destino_entrada.stem + f".{contador}")
            if not novo_nome.exists():
                destino_entrada = novo_nome
                break
            contador += 1

    shutil.move(str(origem), str(destino_entrada))
    
    destino_backup = backup_dir / destino_entrada.name
    return destino_entrada, destino_backup

def mover_para_backup(origem: Path, destino: Path):
    
    if destino.exists():
        contador = 1
        while True:
            novo_destino = destino.with_stem(destino.stem + f".{contador}")
            if not novo_destino.exists():
                destino = novo_destino
                break
            contador += 1
    shutil.move(str(origem), str(destino))


def capturar_arquivos_envio_safra(entrada_dir):
    
    #Declara lista para armazenar o caminho completo dos arquivos
    caminho_arquivo_completo = []

    for file in os.listdir(entrada_dir):
            
        caminho_atual = os.path.join(entrada_dir, file)

        if os.path.isfile(caminho_atual) and caminho_atual.endswith(".txt"): 
            if file.startswith("RETORNO_") and "FLASHCOU" in file:
                
                #Remove "RETORNO_" e "FLASHCOU" da nomenclatura e adiciona "M" no começo
                nova_nomenclatura =  "M" + file.replace("RETORNO_", "").replace("FLASHCOU", "") 
                
                novo_caminho = os.path.join(entrada_dir, nova_nomenclatura)

                #Renomeando o arquivo
                os.rename(caminho_atual, novo_caminho)
                    
                #Armazena o novo caminho/arquivo na lista 
                caminho_arquivo_completo.append(novo_caminho)

                print(f"Arquivo renomeado de {caminho_atual} para {novo_caminho}")

                nomenclatura_arquivos = [os.path.basename(caminho) for caminho in caminho_arquivo_completo]

            else:
                print(f"Não há alterações a serem feitas no arquivo: {file}")
                caminho_atual = os.path.join(entrada_dir, file)
                #Adiciona o novo caminho/arquivo na lista
                caminho_arquivo_completo.append(caminho_atual)

                nomenclatura_arquivos = [os.path.basename(caminho) for caminho in caminho_arquivo_completo]

    return caminho_arquivo_completo, ", ".join(nomenclatura_arquivos)