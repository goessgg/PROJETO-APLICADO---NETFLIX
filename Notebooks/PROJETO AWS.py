import pandas as pd

# Dados fictícios para o modelo de controle de pedidos (podem ser substituídos por dados reais)
clientes = {
    'id_cliente': [1, 2, 3, 4],
    'nome_cliente': ['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D'],
    'email': ['a@exemplo.com', 'b@exemplo.com', 'c@exemplo.com', 'd@exemplo.com']
}

vendedores = {
    'id_vendedor': [1, 2],
    'nome_vendedor': ['Vendedor X', 'Vendedor Y']
}

produtos = {
    'id_produto': [101, 102, 103],
    'nome_produto': ['Produto 1', 'Produto 2', 'Produto 3'],
    'preco': [50, 100, 150]
}

pedidos = {
    'id_pedido': [1001, 1002, 1003, 1004],
    'id_cliente': [1, 2, 1, 3],
    'id_vendedor': [1, 2, 1, 1],
    'id_produto': [101, 102, 103, 101],
    'quantidade': [2, 1, 3, 5],
    'data_pedido': ['2024-09-10', '2024-09-12', '2024-09-14', '2024-09-15']
}

# Criando os DataFrames
df_clientes = pd.DataFrame(clientes)
df_vendedores = pd.DataFrame(vendedores)
df_produtos = pd.DataFrame(produtos)
df_pedidos = pd.DataFrame(pedidos)

# Exibir os DataFrames criados
print("Clientes:\n", df_clientes)
print("\nVendedores:\n", df_vendedores)
print("\nProdutos:\n", df_produtos)
print("\nPedidos:\n", df_pedidos)

# Realizar um merge para unir os dados de pedidos com os dados de clientes, vendedores e produtos
df_pedidos_completo = df_pedidos.merge(df_clientes, on='id_cliente') \
                                .merge(df_vendedores, on='id_vendedor') \
                                .merge(df_produtos, on='id_produto')

# Exibir o DataFrame completo
print("\nPedidos completos:\n", df_pedidos_completo)

# Exemplo de operação: calcular o valor total de cada pedido
df_pedidos_completo['valor_total'] = df_pedidos_completo['quantidade'] * df_pedidos_completo['preco']

# Exibir os pedidos com o valor total
print("\nPedidos com valor total:\n", df_pedidos_completo[['id_pedido', 'nome_cliente', 'nome_vendedor', 'nome_produto', 'quantidade', 'valor_total']])

# Filtrar pedidos por cliente específico
cliente_filtrado = df_pedidos_completo[df_pedidos_completo['nome_cliente'] == 'Cliente A']
print("\nPedidos do Cliente A:\n", cliente_filtrado)

# Agrupar por vendedor e calcular o total de vendas de cada um
vendas_por_vendedor = df_pedidos_completo.groupby('nome_vendedor')['valor_total'].sum().reset_index()
print("\nTotal de vendas por vendedor:\n", vendas_por_vendedor)

# Salvar os dados completos de pedidos em um arquivo CSV
df_pedidos_completo.to_csv('pedidos_completos.csv', index=False)
