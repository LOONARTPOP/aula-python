import plyer
from plyer import notification
import time
import tkinter as tk

janela = tk.tk()
janela.title ("Lembrete")
janela.minsize (200, 300)

def lembrete():
    titulo = "beber aqua"
    mensagem = "subnaqua"
    notification.notify(message=mensagem, title=titulo)
    timeout=5
lembrete()
