import base64
from pathlib import Path

def capturar_anexo_email(caminho_arquivo: str, nome_arquivo: str, tipo: str = "application/octet-stream") -> dict:
    caminho_completo = Path(caminho_arquivo) / nome_arquivo

    if not caminho_completo.exists():
        raise FileNotFoundError(f"O arquivo {caminho_completo} não foi encontrado.")
    
    with open(caminho_completo, "rb") as file:   
        conteudo_base64 = base64.b64encode(file.read()).decode()

    return {
        "name": nome_arquivo,
        "type": tipo,  # ou outro MIME type se souber
        "content": conteudo_base64,
   }