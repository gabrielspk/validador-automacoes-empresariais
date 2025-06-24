def validar_registros(relatorio_df):
    
    def buscar(categoria):
        linha = relatorio_df[relatorio_df['Categoria'] == categoria]
        return linha['Quantidade'].values[0] if not linha.empty else None

    divergencias = []

    original = buscar('Total Registros Originais')
    phoenix = buscar('Total Registros Phoenix')
    concatenado = buscar('Total Registros Concatenados')
    fpl = buscar('Total Registros FPL')
    parte2 = buscar('Total FPLs concatenados')
    parte3 = buscar('Total FPLs enviados ao manuseio')

    if original != phoenix:
        divergencias.append(f"❌ Divergência entre Original ({original}) e Phoenix ({phoenix})")
    
    if original != concatenado:
        divergencias.append(f"❌ Divergência entre Original ({original}) e Concatenado ({concatenado})")
    
    if concatenado != fpl:
        divergencias.append(f"❌ Divergência entre Concatenado ({concatenado}) e FPL ({fpl})")
    
    if parte2 != parte3:
        divergencias.append(f"❌ Divergência entre Parte 2 ({parte2}) e Parte 3 ({parte3})")

    return divergencias