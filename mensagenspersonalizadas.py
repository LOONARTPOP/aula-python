import random #importa a biblioteca de operações aleatórias
import time #importa biblioteca de operações de tempo

listanome = [] #cria variavel pra armazenar a lista

while True: #laço de repetição para caso a ação for verdadeira
    listanome.append(input('Digite um nome: ')) #recebe as informações declaradas pelo usuário
    maisnomes = input("Deseja continuar? ").lower() #recebe a informação se o usuario deseja parar de declarar informações
    if maisnomes == "n": #se a resposta for "n", o codigo vai terminar e seguir com a segunda parte
        break   
def msg(lista): #define a função para randomizar a lista
    print(f"salve {random.choice(lista)}") # codigo para imprimir a frase com um valor aleatorio da lista
    time.sleep(2) # tempo de pausa de uma frase pra outra
    print("vdd")
    time.sleep(2)
    print("girl the boycott")
msg(listanome) #chama a funcao da lista

