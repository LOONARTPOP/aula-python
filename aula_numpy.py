import numpy as np

array_letras = np.array(['a','b','c','d','e'])

print(array_letras)

#Acessando posições especificas
print(array_letras[2])

#Acessando partes do array
print(array_letras[0:3])

#criando um array de inteiros
precos = np.array([20,40,25,35,30])
print("Preços: ", precos)

#Aumentando o preço de todos os valores do array em 10%
novos_precos = precos * 1.1
print("Valor aumentado:> ", novos_precos)

#Soma de todos os preços do array precos
total_vendas = np.sum(precos)

#Média dos preços
media_precos = np.mean(precos)
print("A média de preços do array:> ", media_precos)

#maior e menor valor do array
maior_valor = np.max(precos)
menor_valor = np.min(precos)

print("Maior preço do array: ", maior_valor)
print("Menor preço do array: ", menor_valor)

#Gerador de números aleatórios

rng = np.random.default_rng()
#print(rng.random(4_00) * 100)

#Exercicio
#Gere 500.000 numeros aleatorios
#mostre o maior e o menor valor do array
#mostre a media dos valores
print("-----------Exercício-----------")
array_brincando = np.array(rng.random(500_000) * 4_000)

menornum = np.min(array_brincando)
maiornum = np.max(array_brincando)
mediaval = np.mean(array_brincando)

print("Menor número: ", menornum, "\nMaior número: ", maiornum, "\nMédia dos valores: ", mediaval)
