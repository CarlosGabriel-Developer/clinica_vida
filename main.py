from datetime import datetime

ano_atual = datetime.today().year

banco_dados_pacientes = []

paciente = {}


print ("-"*40)

while True : 
    
    cadastrar_paciente = str(input("Deseja continuar [S/N]: "))
    
    if cadastrar_paciente not in "Ss" :
        print("Fim do Programa") 
        break
    
print ("-"*40)