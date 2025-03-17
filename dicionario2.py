produto = {
    'nome': ['Feijão', 'Arroz', 'Farinha'],
    'quantidade': [],
    'preço': [500,1000,2]
}
for nome, quantidade, preço in zip(produto['nome'],produto['quantidade'],produto['preço']):
    print("Produto:", nome,"Quantidade:", quantidade,"Preço:",preço)