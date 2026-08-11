from datetime import datetime

ano_atual = datetime.today().year

banco_dados_pacientes = []

paciente = {}


print ("-"*40)

print("=== SISTEMA CLÍNICA VIDA+ ===")
print('[1] CADASTRAR PACIENTE')
print('[2] VER ESTATÍSTICAS')
print('[3] BUSCAR PACIENTE')
print('[4] LISTA DE TODOS OS PACIENTES')
print('[5] SAIR')

print ("-"*40)

usuario_escolha = int(input('ESCOLHA UMA OPÇÃO ENTRE 1 - 5 : '))

if usuario_escolha == 1 : 
    
    print('=== CADASTRAR PACIENTE ===')
    print ("-"*40)
    
    paciente['Nome'] = str(input('NOME DO PACIENTE: ')).upper()
    
    paciente['Idade'] = int(input('ANO DE NACIMENTO DO PACIENTE: '))
    
    paciente['Telefone'] = str(input('TELEFONE (DDD) XXXXX-XXXX: '))
    
    

while True : 
    
    cadastrar_paciente = str(input("Deseja continuar [S/N]: "))
    
    if cadastrar_paciente not in "Ss" :
        print("Fim do Programa") 
        break
    
print ("-"*40)