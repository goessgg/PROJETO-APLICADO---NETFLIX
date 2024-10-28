import pandas as pd

# Carregar a planilha Excel
file_path = r'C:\FACULDADE\PROJETO APLICADO\PROJETO NETFLIX\BASE - NETFLIX.xlsx'
df = pd.read_excel(file_path, sheet_name='BASE - NETFLIX')


# Função para gerar a tabela hierarquizada por país
def gerar_tabela_pais(pais_escolhido):
    df_pais = df[df['País'].str.lower() == pais_escolhido.lower()]  # Faz a busca sem case sensitive

    if df_pais.empty:
        print(f"Não há dados para o país: {pais_escolhido}")
        return

    # Agrupar por Gênero, Tipo de assinatura, Dispositivo e somar os valores da assinatura
    pivot_table = df_pais.groupby(['Gênero', 'Tipo de assinatura', 'Dispositivo Utilizado'])[
        'Valor da assinatura/mês'].sum()

    # Converter para DataFrame e formatar valores de forma monetária
    pivot_table_df = pivot_table.reset_index()
    pivot_table_df['Valor da assinatura/mês'] = pivot_table_df['Valor da assinatura/mês'].apply(
        lambda x: f"R$ {x:,.2f}")

    # Exibir a tabela gerada
    print(f"\nTabela de análise para {pais_escolhido}:\n")
    print(pivot_table_df.to_string(index=False))


# Função para listar países e pedir a escolha
def listar_paises_e_perguntar():
    # Listar os países únicos
    paises_unicos = df['País'].unique()

    while True:  # Loop contínuo até o usuário escolher sair
        print("\nPaíses disponíveis para análise:\n")

        for i, pais in enumerate(paises_unicos, 1):
            print(f"{i}. {pais}")

        print("\nDigite o nome ou número do país que você deseja consultar (ou 'sair' para encerrar): ")
        pais_escolhido = input().strip()

        # Verificar se o usuário quer sair do loop
        if pais_escolhido.lower() == 'sair':
            print("Encerrando o programa...")
            break

        # Verificar se o usuário digitou o número ou o nome do país
        if pais_escolhido.isdigit():
            try:
                pais_escolhido = paises_unicos[int(pais_escolhido) - 1]
            except IndexError:
                print("Número inválido. Tente novamente.")
                continue  # Pede ao usuário para tentar novamente

        # Exibir a tabela do país escolhido
        gerar_tabela_pais(pais_escolhido)


# Executar o processo
listar_paises_e_perguntar()
