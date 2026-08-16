from datetime import datetime

ano_atual = datetime.today().year

banco_dados_pacientes = []

print ("-"*40)

print("=== SISTEMA CLÍNICA VIDA+ ===")
print('[1] CADASTRAR PACIENTE')
print('[2] VER ESTATÍSTICAS')
print('[3] BUSCAR PACIENTE')
print('[4] LISTA DE TODOS OS PACIENTES')
print('[5] SAIR')

print ("-"*40)

usuario_escolha = str(input('ESCOLHA UMA OPÇÃO ENTRE 1 - 5 : '))

if usuario_escolha == "1" : 
    
    paciente = {}

    print('=== CADASTRAR PACIENTE ===')
    print ("-"*40)

    paciente['Nome'] = str(input('NOME DO PACIENTE: ')).upper()
    
    while True : 
    
        paciente_ano_nacimento = int(input('ANO DE NACIMENTO DO PACIENTE: '))
        
        idade = datetime.today().year - paciente_ano_nacimento
        
        if 0 <= idade <= 120 : 
            paciente['Idade'] = idade
            break
        
        else : 
            print('ANO DE NASCIMENTO INVÁLIDO')
        
    paciente['Telefone'] = str(input('TELEFONE (DDD) XXXXX-XXXX: '))
        
    banco_dados_pacientes.append(paciente)
    
    print('PACIENTE CADASTRADO COM SUCESSO')
    
    print ("-"*40)
    
elif usuario_escolha == '2':
    
    numero_pacientes_cadastrados = 0
    paciente_mais_novo = None
    paciente_mais_velho = None

for paciente in banco_dados_pacientes:
    numero_pacientes_cadastrados += 1

    if paciente_mais_velho is None or paciente['Idade'] > paciente_mais_velho:
        paciente_mais_velho = paciente['Idade']

    if paciente_mais_novo is None or paciente['Idade'] < paciente_mais_novo:
        paciente_mais_novo = paciente['Idade']
    
while True : 
    
    cadastrar_paciente = str(input("Deseja continuar [S/N]: "))
    
    if cadastrar_paciente not in "Ss" :
        print("Fim do Programa") 
        break
    
print ("-"*40)