import tkinter as tk
import pyautogui
import time
import plyer
from plyer import notification

if __name__=="__main__":
 
        notification.notify(
            title = "BORA BEBER AGUA",
            message=" hora de beber agua" ,
            
            # tempo de tela
            timeout=2
)
        # tempo de espera
        time.sleep(2)