def eh_par(numero):
    return numero % 2 == 0
numero= int(input("Digite um numero:"))
print(eh_par(numero))

#exercicios com Booleanos
idade= int(input("Digite a sua idade:"))
idd= int(input("Digite a sua idade:"))


if idade > idd:
    print(f"A idade(idade) é maior que (idd)")

else:
   print(f"A idade (idd) é maior que")

def idadeMaior(idade1,idade2):
    return idade1>idade2

idade1 = int(input("digite a primeira idade:"))
idade2 = int(input("digite a segunda idade:"))

idadeMaior(idade1, idade2)
print(idadeMaior(idade1,idade2))