import pandas as pd
dadosProdutos = pd.read_csv("produtos.csv")
print(dadosProdutos)


#calcula a media

import pandas as pd
dadosProdutos = pd.read_csv("produtos.csv")
dadosProdutos['PRECO'].max()
print("Média dos preços dos produtos ", dadosProdutos['PRECO'].mean())

#victoria carvalho
