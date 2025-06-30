def formatar_corpo_html(tabela_html, divergencias):
    estilo_base = """
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333;
            font-size: 15px;
            line-height: 1.6;
        }}
        h2 {{
            font-size: 18px;
            margin-top: 30px;
            color: #1a1a1a;
        }}
        p {{
            margin: 16px 0;
            font-size: 14px;
        }}
        ul {{
            margin: 10px 0 20px 20px;
        }}
        li {{
            margin-bottom: 8px;
        }}
    </style>
    """

    if divergencias:
        lista_erros = "<ul>" + "".join([f"<li>{erro}</li>" for erro in divergencias]) + "</ul>"
        corpo = f"""
        <p><strong style="color: #d9534f;">Foram encontradas divergências:</strong></p>
        {lista_erros}
        {tabela_html}
        """
    else:
        corpo = f"""
        <p style="color: #3c763d;"><strong>Validação realizada com sucesso.</strong> Nenhuma divergência foi encontrada.</p>
        {tabela_html}
        """

    return f"<html><head>{estilo_base}</head><body>{corpo}</body></html>"

def formatar_corpo_html_safra(data: str = None, hora: str = None, erro: str = None, sucesso: bool = True) -> str:
    estilo_base = """
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333;
            font-size: 15px;
            line-height: 1.6;
        }}
        p {{
            margin: 16px 0;
            font-size: 14px;
        }}
        .sucesso {{
            color: #3c763d;
            font-weight: bold;
        }}
        .erro {{
            color: #d9534f;
            font-weight: bold;
        }}
        pre {{
            background-color: #f8d7da;
            padding: 10px;
            border-radius: 5px;
            white-space: pre-wrap;
            font-family: monospace;
            font-size: 13px;
        }}
    </style>
    """

    if sucesso:
        corpo = f"""
        <p class="sucesso">✅ O RPA foi executado com sucesso.</p>
        <p>O arquivo de data <strong>{data}</strong> gerado às: <strong>{hora}</strong> foi enviado corretamente.</p>
        <p>Print da evidência do envio em anexo.</p>
        """
    else:
        corpo = f"""
        <p class="erro">❌ Ocorreu um erro durante a execução do RPA:</p>
        <pre>{erro}</pre>
        """

    return f"<html><head>{estilo_base}</head><body>{corpo}</body></html>"