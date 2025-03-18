import pyautogui
import time

def enviar_mensagem(mensagem, numero):
    print(f"Abrindo chat com {numero}...")
    link = f"https://web.whatsapp.com/send?phone={numero}"
    pyautogui.hotkey('ctrl', 't')  # Abre uma nova aba
    time.sleep(1)
    pyautogui.write(link)
    pyautogui.press('enter')
    
    time.sleep(10)  # Tempo para carregar o WhatsApp Web
    pyautogui.write(mensagem)
    pyautogui.press('enter')
    print("Mensagem enviada com sucesso!")

def menu():
    print("\nEscolha um tipo de mensagem:")
    print("1 - Mensagem de Bom Dia")
    print("2 - Mensagem de Motivação")
    print("3 - Mensagem Personalizada")
    escolha = input("Digite o número da opção: ")
    return escolha

def main():
    numero = input("Digite o número de telefone com DDD (ex: +5511999999999): ")
    escolha = menu()
    
    if escolha == "1":
        mensagem = "Bom dia! Espero que tenha um dia maravilhoso! ☀️"
    elif escolha == "2":
        mensagem = "Nunca desista dos seus sonhos! O sucesso está mais perto do que imagina. 💪"
    elif escolha == "3":
        mensagem = input("Digite sua mensagem personalizada: ")
    else:
        print("Opção inválida!")
        return
    
    enviar_mensagem(mensagem, numero)

if __name__ == "__main__":
    main()
