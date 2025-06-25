def validar_registros(relatorio_df, qtde_arquivos_rem):
    def buscar(categoria):
        linha = relatorio_df[relatorio_df['Categoria'] == categoria]
        return linha['Quantidade'].values[0] if not linha.empty else None
    
    divergencias = []

    remessa = buscar('Total registros remessa')
    fpl = buscar('Total registros fpl')

    if remessa != fpl:
        divergencias.append(f"❌ Divergência entre remessa ({remessa}) e FPL ({fpl})")

    if qtde_arquivos_rem < 3:
        divergencias.append(f"❌ Deveria ter sido recebido 3 arquivos diários, foram recebidos {qtde_arquivos_rem}")
    
    return divergencias
    