#✅ 5. Gráficos automáticos (usando matplotlib ou seaborn)
#Gerar gráfico de barras com produtos e quantidade vendida.
#Salvar como imagem grafico.png para usar em relatório.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("vendas.csv")

resumo_vendas = df.groupby("Produto")["Quantidade"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(x="Produto", y="Quantidade",  data=resumo_vendas, palette="viridis")

plt.title("Total de vendas por produto", fontsize=14)
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.savefig("grafico.png", dpi=300, bbox_inches="tight")
plt.show()

print("\n✅ Gráfico 'grafico.png' gerado com sucesso!")