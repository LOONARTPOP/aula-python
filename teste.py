import pandas as pd
import matplotlib.pyplot as plt

# Dados para plotar
labels = 'tipo_cultivo','produtividade','uso_agua','custo_medio','ano'
tamanhos = [1215, 2130, 2245, 2210]

# definições
colors = ['lightcoral','gold', 'yellowgreen',  'lightskyblue']

# explodir 1ª fatia
explode = (0.1, 0, 0, 0)  

# Plot
plt.pie(tamanhos, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
