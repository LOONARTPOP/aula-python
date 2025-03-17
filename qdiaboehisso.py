import pandas as pd
import matplotlib.pyplot as plt

dados_produtos = pd.read_csv('produtos2.csv', delimiter=',') #carregando dados
print(dados_produtos.columns)
plt.figure(figsize=(10, 6)) #criando grafico de preço por ano para cada produto

for produto in dados_produtos['produto'].unique(): #plotando os dados para cada produto
    dados_produtos = dados_produtos[dados_produtos['produto'] == produto]
    plt.plot(dados_produtos['Ano'], dados_produtos['preco'], label=produto, marker='o')

# Adicionando titulo e rótulos
plt.title('Preço dos Produtos ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Preço')
plt.legend(title='Produto')

# exibindo o grafico
plt.grid(True)
plt.show()

# importação de bibliotecas pandas e matplotlib
# carregue os dados com o pandas
# crie uma figura com o pyplot
# usando o for para cada produto, sera buscado o preco e o ano
# plot o preco e ao de cada produto no grafico
# adicione o titulo do grafico
# adicione o titulo de eixo x que sera o ano
# adicione o titulo do eixo y que sera o preço
# apresentar o grafico com a funcao show()