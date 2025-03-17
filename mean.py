#calcula a media

import pandas as pd
dadosProdutos = pd.read_csv("produtos2.csv")
print(dadosProdutos.columns)

dadosProdutos['preco'].max()
print("Média dos preços dos produtos ", dadosProdutos['preco'].mean())