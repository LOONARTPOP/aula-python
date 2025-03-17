produto = {
    'Nome:': 'Feijão',
    'Quantidade': 10,
}

nome = produto ['Nome:']
quantidade = produto ['Quantidade']
print("Nome: ", nome)
print('Quantidade: ', quantidade)

#Alterando
produto['Quantidade'] = 100

quantidade = produto['Quantidade']

print('Nome: ', nome)
print('Quantidade: ', quantidade)

for chave, valor in produto.items():
    print(chave, valor)

#Adicionando
produto = {
    'Nome': ['Feijão', 'Arroz', 'Farinha'],
    'Quantidade': [10,10, 100]
}

for chave, valor in produto.items():
    print(chave, valor)

#função zip tem como finalidade juntar duas listas com suas respectivas posições

for nome, quantidade in zip(produto['Nome'], produto['Quantidade']):
    print("Produto:", nome, "Quantidade: ", quantidade)
#Victória Beatriz Bacelar de Carvalho