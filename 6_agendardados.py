#✅ 6. Agendar execução automática (usando schedule ou task scheduler)
#Criar uma tarefa automática que execute o script de análise todo dia às 9h.


import schedule
import time
import subprocess

def executar_analise():
    print("\n Executando análise de vendas...")
    subprocess.run(["python, leia.py"]) #substituir pelo nome do script

schedule.every().day.at("06:45").do(executar_analise)
print("Aguardando horario programado para executar o script...")

while True:
    schedule.run_pending()
    time.sleep(60)