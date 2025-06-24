def validar_registros(relatorio_df):
    def buscar(categoria):
        linha = relatorio_df[relatorio_df['Categoria'] == categoria]
        return linha['Quantidade'].values[0] if not linha.empty else None

    divergencias = []

    original = buscar('Total Registros Originais')
    concatenado = buscar('Total Registros Concatenados')
    fpl = buscar('Total Registros FPL')

    if original != concatenado:
        divergencias.append(f"❌ Divergência entre Original ({original}) e Concatenado ({concatenado})")
    
    if concatenado != fpl:
        divergencias.append(f"❌ Divergência entre Concatenado ({concatenado}) e FPL ({fpl})")

    return divergencias