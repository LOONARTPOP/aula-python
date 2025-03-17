lista = [14,64,674,84,78,94,324]
lista.sort(reverse=True)
print(lista)

maiorElemento = max(lista)
print("Maior elemento da lista:", maiorElemento)

lista.append(2)     #Número 2 adicionado
menorElemento = min(lista)
print("Lista atualizada:", lista) 
print("Menor elemento da lista:", menorElemento)    #Exibe menor elemento da lista
lista.append(6)
lista.append(25)    #Números 6 e 25 adicionados
print("Lista atualizada:", lista)
print("Elemento da posição 3:", lista[2]) #Mostra o elemento 2 da lista

listaDobro = []
for item in lista:
    listaDobro.append(item * 2) #Lista com itens dobrados

print("Lista: ", lista)
print("Lista dobrada:", listaDobro)

#Victória Beatriz Bacelar de Carvalho