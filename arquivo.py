with open("texto.txt", "w", encoding="utf-8") as file:
    for i in range(3):
        frase = input (f"Digite a {i+1}ª frase: ")
        file.write(frase + "\n")
print ("Frases salvas com sucesso!")



# w significa write
# encoding / codigo q o vs code entende utf-8 (pesquisar mais sobre)
# range - inserir 3 linhas
# f vai puxar o que tem na chave


#fazer ler o programa