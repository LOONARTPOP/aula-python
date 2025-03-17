numerosPares = 0
numerosImpares = 0   

for i in range(5):      
   numero = (input("Digite um número: "))    

   if numero % 2 == 0: #Número é par
      numerosPares = numerosPares + 1
   else:
      numerosImpares = numerosImpares + 1

print(f"Quantidade de pares: ", (numerosPares))
print(f"Quantidade de Impares: ", (numerosImpares))

for i in range(numerosPares):
   print(numerosPares)
#Victória Beatriz Bacelar de Carvalho