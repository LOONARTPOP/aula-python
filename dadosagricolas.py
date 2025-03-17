# importação de bibliotecas pandas e matplotlib
# carregue os dados com o pandas
# crie uma figura com o pyplot
# usando o for para cada produto, sera buscado o preco e o ano
# plot o preco e ao de cada produto no grafico
# adicione o titulo do grafico
# adicione o titulo de eixo x que sera o ano
# adicione o titulo do eixo y que sera o preço
# apresentar o grafico com a funcao show()

import pandas as pd
import matplotlib.pyplot as plt

dadosTabela = pd.read_csv("dados.csv", delimiter=',')
plt.figure(figsize=(15,8))

for tipo_cultivo in dadosTabela['tipo_cultivo'].unique():
    dadosTabela = dadosTabela[dadosTabela['tipo_cultivo'] == tipo_cultivo]
    plt.plot(dadosTabela['ano'],dadosTabela['produtividade'], label=tipo_cultivo, marker='o')

plt.title('PRODUÇÃO AGRÍCOLA')
plt.xlabel('Ano')
plt.ylabel('Produtividade')
plt.legend(title='Produto')

# exibindo o grafico
plt.grid(True)
plt.show()





#for uso_agua in dadosTabela['uso_agua'].unique():
#    dadosTabela3 = dadosTabela[dadosTabela['uso_agua'] == uso_agua ]
#    plt.plot(dadosTabela2['uso_agua'], label=tipo_cultivo, marker='x')