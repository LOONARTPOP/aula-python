#Lista de Exercícios – Automação com Análise de Dados (Python)

#✅ 1. Leitura e análise de CSV
#Ler um arquivo vendas.csv com colunas: Produto, Quantidade, Preço.
#Calcular o total vendido por produto.
#Gerar um relatório com o produto mais vendido.

import pandas as pd


tabela_vendas = pd.read_csv("vendas.csv", delimiter=";")


valor_unitario = (tabela_vendas["PrecoUnit"])
quant_vendida = (tabela_vendas["Quantidade"])

valor_total_vendas = valor_unitario * quant_vendida


indice = tabela_vendas["PrecoUnit"].idxmax() # Obtendo o produto com maior preço
produto_maior_preco = tabela_vendas.loc[indice, "Produto"]
preco = tabela_vendas.loc[indice, "PrecoUnit"]


print(tabela_vendas.loc["Produto"], valor_total_vendas)

print("Produto com a maior quantidade: ", produto_maior_preco, "com", preco , "unidades ")

