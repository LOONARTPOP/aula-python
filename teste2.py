import pandas as pd

dadosProdutos = pd.read_csv("produtos2.csv") 

indice = dadosProdutos["preco"].idxmax() # Obtendo o produto com maior preço
produto_maior_preco = dadosProdutos.loc[indice, "produto"]
preco = dadosProdutos.loc[indice, "preco"]

print("Produto com a maior quantidade: ", produto_maior_preco, "com", preco , "unidades ")