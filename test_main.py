from datetime import datetime
    
banco_dados_pacientes = []



usuario_escolha = str(input('ESCOLHA UMA OPÇÃO ENTRE 1 - 5 : '))

if usuario_escolha == "1" : 
    
    paciente = {}
    
    print('=== CADASTRAR PACIENTE ===')
    
    paciente['Nome'] = str(input('NOME DO PACIENTE: ')).upper()
    
    while True : 
    
        paciente_ano_nacimento = int(input('ANO DE NACIMENTO DO PACIENTE: '))
        
        idade = paciente_ano_nacimento - datetime.today().year
        
        if 0 <= idade <= 120 : 
            paciente['Idade'] = idade
            break
        
        else : 
            print('ANO DE NASCIMENTO INVÁLIDO')
        
    paciente['Telefone'] = str(input('TELEFONE (DDD) XXXXX-XXXX: '))
        
    banco_dados_pacientes.append(paciente)
    
    print('PACIENTE CADASTRADO COM SUCESSO')
    
    
    
