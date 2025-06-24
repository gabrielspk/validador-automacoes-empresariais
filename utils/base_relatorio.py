import pandas as pd

def gerar_tabela_html(df):
    df["Categoria"] = pd.Categorical(df["Categoria"], categories=df["Categoria"].unique(), ordered=True)
    df_agrupado = df.groupby("Categoria", as_index=False)["Quantidade"].sum()
    df_agrupado["Quantidade"] = df_agrupado["Quantidade"].apply(lambda x: f"{x:,.0f}".replace(",", "."))

    html = """
    <h2 style="font-family: Arial, sans-serif; color: #333;">📊 Resumo do Relatório</h2>
    <table style="width: 100%; max-width: 600px; border-collapse: collapse; font-family: Arial, sans-serif; font-size: 14px; color: #333;">
      <thead>
        <tr style="background-color: #f2f2f2;">
          <th style="padding: 10px; border: 1px solid #ddd; text-align: left;">Categoria</th>
          <th style="padding: 10px; border: 1px solid #ddd; text-align: right;">Quantidade</th>
        </tr>
      </thead>
      <tbody>
    """

    for _, row in df_agrupado.iterrows():
        html += f"""
        <tr>
          <td style="padding: 10px; border: 1px solid #ddd;">{row['Categoria']}</td>
          <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">{row['Quantidade']}</td>
        </tr>
        """

    html += """
      </tbody>
    </table>
    """

    return html