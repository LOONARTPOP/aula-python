salario_atual = float(input("Digite o salário atual: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))
salario_novo = salario_atual + (salario_atual * porcentagem_aumento/100)

print("Novo valor de salário: R$", salario_novo)
