import pandas as pd

def gerar_relatorio(df):

    df = df[~df['Processo'].str.contains('ITAU_ENVIOPOSVENDASAR', na=False)]
    
    registros_remessa = df[df['Nome Arquivo'].str.contains('REMESSA', na=False)]
    
    registros_status_entregar = df[df['Nome Arquivo'].str.contains('REMESSA', na=False) & 
                                   df['Status'].str.contains('Entregar', na=False)]
    
    registros_status_parados = df[df['Nome Arquivo'].str.contains('REMESSA', na=False) & 
                                  df['Status'].str.contains('Parado', na=False)]
    
    registros_fpl = df[df['Nome Arquivo'].str.contains('ITAU_VALIDACAO', na=False)]
    
    total_arquivos_remessa = len(registros_remessa)

    total_arquivos_entregar = len(registros_status_entregar)
    total_arquivos_parados = len(registros_status_parados)

    total_registros_remessa = registros_remessa['Registros'].sum()
    total_registros_fpl = registros_fpl['Registros'].sum()

    categorias = ['Total registros remessa', 'Total registros fpl']
    quantidades = [total_registros_remessa, total_registros_fpl]

    idx = 1
    if total_arquivos_entregar > 0:
        categorias.insert(1, 'Registros status a entregar')
        quantidades.insert(1, total_arquivos_entregar)
        idx+=1
    
    if total_arquivos_parados > 0:
        categorias.insert(idx, 'Registros status parado')
        quantidades.insert(1, total_arquivos_parados)

    print(registros_remessa.head())
    print(registros_fpl.head())
    print(df.columns)
    print(df.dtypes)


    return pd.DataFrame({'Categoria': categorias, 'Quantidade': quantidades}), total_arquivos_remessa