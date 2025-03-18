import random #importa a biblioteca de operações aleatórias
import time #importa biblioteca de operações de tempo
import pyautogui as ag

usuario = input(f"Digite seu nome: ")

listafrases = [] #cria variavel pra armazenar a lista

while True: #laço de repetição para caso a ação for verdadeira
    listafrases.append(input('Digite uma frase: ')) #recebe as informações declaradas pelo usuário
    maisnomes = input("Deseja continuar? ").lower() #recebe a informação se o usuario deseja parar de declarar informações
    if maisnomes == "n": #se a resposta for "n", o codigo vai terminar e seguir com a segunda parte
        break   

print(f"Olá {usuario}! selecione uma frase a ser exibida")


print(listafrases)


# def msg(lista): #define a função para randomizar a lista
#    print(f"salve {random.choice(lista)}") # codigo para imprimir a frase com um valor aleatorio da lista
#    time.sleep(2) # tempo de pausa de uma frase pra outra
#    print("vdd")
#    time.sleep(2)
#    print("girl the boycott")
#msg(listanome) #chama a funcao da lista

