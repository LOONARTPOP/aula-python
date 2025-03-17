#entre com valor unitario do produto, entre com a quntidade, o programa retornar com o valor total sem desconto
# o programa deve retornar o valor total apos o desconto, deve user estruturas if elif e else // .2f valor tipo float
quantidade = int(input("Digite a quantidade: "))
valor = float(input("Digite o valor: "))

if quantidade < 5:
    desconto = 0
elif quantidade < 10:
    desconto = 0.1
else:
    desconto = 0.2
#variaveis
valorsemdesconto = quantidade*valor
valorcomdesconto = valor * (1 - desconto)
valortotal = quantidade * valorcomdesconto
valordesconto = quantidade * valor * desconto
porcentagemsemdesconto = desconto * 100

#saida de dados:
print(f'valor sem desconto: ', valorsemdesconto)
print(f"valor unitario: R$ {valor: .2f}")
print(f'valor com desconto: R$ {valortotal: .2f}')