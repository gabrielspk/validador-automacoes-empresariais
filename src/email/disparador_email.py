import requests
from requests.structures import CaseInsensitiveDict
import json
from config import HOST_SMTP, MAILGRID_USUARIO, MAILGRID_SENHA

def enviar_email(assunto, corpo, destinatarios, anexos=None):
    url = "https://api.mailgrid.net.br/send/"  # endpoint oficial

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    # Construindo os dados como dicionário (melhor para editar antes de converter em JSON string)
    dados = {
        "host_smtp": HOST_SMTP,
        "usuario_smtp": MAILGRID_USUARIO,
        "senha_smtp": MAILGRID_SENHA,
        "emailRemetente": "moovemais@moovemais.com.br",
        "nomeRemetente": "moovemais",
        "emailDestino": destinatarios,
        "assunto": f"{assunto}",
        "mensagem": f"{corpo}",
        "mensagemAlt": "Olá! Segue relatório com os dados abaixo: Registros: 28.713",
        "mensagemTipo": "html",
        "mensagemEncoding": "quoted-printable"
    }

    if anexos:
        dados["mensagemAnexos"] = {
            f"file{i+1}": {
                "name": anexo["nome"],
                "type": anexo["tipo"],
                "content": anexo["conteudo"]
            } for i, anexo in enumerate(anexos)
        }

    # Convertendo para JSON string, como a API exige
    data_json = json.dumps(dados)

    # Enviando a requisição
    resp = requests.post(url, headers=headers, data=data_json)

    if resp.status_code == 200:
        print("✅ E-mail enviado com sucesso!")
        print(resp.json())  # mostra o JSON de retorno
    else:
        print("❌ Falha ao enviar e-mail.")
        print("Status:", resp.status_code)
        print("Resposta:", resp.text)