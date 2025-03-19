import random #importa a biblioteca de operações aleatórias
import time #importa biblioteca de operações de tempo


usuario = input(f"Digite seu nome: ")

listafrases = [] #cria variavel pra armazenar a lista

while True: #laço de repetição para caso a ação for verdadeira
    listafrases.append(input('Digite uma frase: ')) #recebe as informações declaradas pelo usuário
    maisnomes = input("Deseja continuar com as frases? ").lower() #recebe a informação se o usuario deseja parar de declarar informações
    if maisnomes == "n": #se a resposta for "n", o codigo vai terminar e seguir com a segunda parte
        break   

print(f"Olá {usuario}! selecione uma frase a ser exibida")

for i,item in enumerate(listafrases, 1): #enumerate pra enumerar a lista 
    print(f"{i}:",item)

while True:
    try: #funçao pra capturar erros dentro do loop
        escolha = int(input("Digite o número da opção: "))  # Converte entrada para inteiro / precisa ser inteiro se nao o try vai capturar
        if 1 <= escolha <= len(listafrases):  # Verifica se esta dentro do intervalo válido
            print(f"Sua frase escolhida foi: {listafrases[escolha - 1]}, {usuario}")  #imprime a frase junto do usuario
            break #encerra o codigo
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError: #funcao except recebe o erro caso ocorra
        print("Entrada inválida! Digite um número válido.")

