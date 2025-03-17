num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1+num2

if soma >= 20:
    print("soma maior que 20: ", soma)
    print("o novo valor é: ", soma + 8)
else:
    print("valor da soma menor que 20: ", soma)
    print("o novo valor é: ", soma - 5)
    
print("Resultado: ", (soma > 20) and (soma < 20))


#Victória Beatriz Bacelar de Carvalho